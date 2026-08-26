/**
 * eleanote ad renderer — deterministic frame-by-frame capture of an ad
 * page (its ?render mode exposes window.__seek/__total) into an MP4.
 *
 *   node render.mjs ad1-copypaste.html                 -> out/ad1-copypaste.mp4
 *   node render.mjs ad1-copypaste.html --stills 1.5,8  -> out/still-*.png proof frames
 *
 * Uses the installed system Chrome via puppeteer-core and the bundled
 * ffmpeg-static binary. 1080x1350 @ 30fps.
 */
import puppeteer from 'puppeteer-core';
import ffmpegPath from 'ffmpeg-static';
import { spawn } from 'node:child_process';
import { mkdirSync, writeFileSync } from 'node:fs';
import { resolve, basename } from 'node:path';

const W = 1080, H = 1350, FPS = 30;
const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';

const pageFile = process.argv[2];
if (!pageFile) { console.error('usage: node render.mjs <page.html> [--stills t1,t2,...]'); process.exit(1); }
const stillsArg = process.argv.indexOf('--stills');
const stills = stillsArg > -1 ? process.argv[stillsArg + 1].split(',').map(Number) : null;

const url = 'file:///' + resolve(pageFile).replace(/\\/g, '/') + '?render';
mkdirSync('out', { recursive: true });

const browser = await puppeteer.launch({
  executablePath: CHROME,
  headless: 'new',
  args: ['--force-device-scale-factor=1', '--hide-scrollbars', '--disable-lcd-text'],
});
const page = await browser.newPage();
await page.setViewport({ width: W, height: H, deviceScaleFactor: 1 });
page.on('console', m => { if (m.type() === 'error') console.error('[page]', m.text()); });
await page.goto(url, { waitUntil: 'networkidle0', timeout: 60000 });
await page.waitForFunction('window.__ready === true', { timeout: 60000 });
const total = await page.evaluate('window.__total');
console.log(`page ready — total ${total}s`);

const clip = { x: 0, y: 0, width: W, height: H };

if (stills) {
  for (const t of stills) {
    await page.evaluate(`window.__seek(${t})`);
    const buf = await page.screenshot({ clip });
    const name = `out/still-${String(t).replace('.', '_')}.png`;
    writeFileSync(name, buf);
    console.log('wrote', name);
  }
  await browser.close();
  process.exit(0);
}

const frames = Math.round(total * FPS);
const outName = 'out/' + basename(pageFile, '.html') + '.mp4';
const ff = spawn(ffmpegPath, [
  '-y', '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-',
  '-c:v', 'libx264', '-preset', 'slow', '-crf', '18',
  '-pix_fmt', 'yuv420p', '-movflags', '+faststart', outName,
], { stdio: ['pipe', 'inherit', 'inherit'] });

const t0 = Date.now();
for (let i = 0; i < frames; i++) {
  const t = i / FPS;
  await page.evaluate(`window.__seek(${t})`);
  const buf = await page.screenshot({ clip });
  if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
  if (i % 90 === 0) {
    const el = ((Date.now() - t0) / 1000).toFixed(0);
    console.log(`frame ${i}/${frames} (t=${t.toFixed(1)}s, elapsed ${el}s)`);
  }
}
ff.stdin.end();
await new Promise((res, rej) => ff.on('close', c => (c === 0 ? res() : rej(new Error('ffmpeg exit ' + c)))));
await browser.close();
console.log('DONE ->', outName);
