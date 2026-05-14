#!/usr/bin/env node
//
// gen-wallpapers.js — generates the mock-laptop "Bloom"-style wallpapers.
//
// Run from the repo root:
//   node tools/gen-wallpapers.js
//
// Outputs:
//   docs/img/wallpaper-d.svg   (desktop / 16:10 stage)
//   docs/img/wallpaper-p.svg   (phone / 9:13 stage)
//
// Each SVG is a teal background + ~40 light curves fanning out from a
// point in the lower-right -- the Windows 11 "Bloom" aesthetic, but
// recoloured to match the brand teal.  Edit the parameters at the
// bottom of this file (origin, theta range, curve count, colours) and
// rerun to tune the look.

const fs = require('fs');
const path = require('path');

function generateSVG({
    width,
    height,
    originX,
    originY,
    thetaMin,         // radians, measured from -Y axis (straight up) CCW
    thetaMax,
    numCurves,
    bgStart = '#225862',
    bgEnd = '#143a42',
    strokeColor = '#dff0f3',
    glowColor = 'rgba(140, 200, 210, 0.20)',
}) {
    const paths = [];
    const R = Math.max(width, height) * 1.6;

    for (let i = 0; i < numCurves; i++) {
        const t = i / (numCurves - 1);
        const theta = thetaMin + t * (thetaMax - thetaMin);

        // Direction unit vector (rotating CCW from "straight up")
        const dx = -Math.sin(theta);
        const dy = -Math.cos(theta);

        // End point well off-canvas so curves run to the edges cleanly.
        const ex = originX + R * dx;
        const ey = originY + R * dy;

        // Perpendicular to direction (rotated 90deg CCW). We use this
        // to bulge the control points away from the straight line so
        // each curve looks like a graceful arc rather than a ray.
        const px = -dy;
        const py = dx;

        // Bulge varies slightly along the fan so the curves don't all
        // bend identically -- gives the pattern a "flowing" feel.
        const bulge = 90 + 55 * Math.sin(i * 0.35);

        const c1x = originX + R * 0.25 * dx + bulge * px;
        const c1y = originY + R * 0.25 * dy + bulge * py;
        const c2x = originX + R * 0.62 * dx + 1.7 * bulge * px;
        const c2y = originY + R * 0.62 * dy + 1.7 * bulge * py;

        // Opacity peaks in the middle of the fan -- gives a bright
        // "highlight band" sweep across the wallpaper.
        const opacity = 0.07 + 0.18 * Math.sin(t * Math.PI);

        // Slight variation in stroke width so the band has texture.
        const sw = 0.7 + 0.35 * Math.cos(i * 0.5);

        paths.push(
            `    <path d="M ${originX} ${originY} ` +
            `C ${c1x.toFixed(0)} ${c1y.toFixed(0)}, ` +
            `${c2x.toFixed(0)} ${c2y.toFixed(0)}, ` +
            `${ex.toFixed(0)} ${ey.toFixed(0)}" ` +
            `opacity="${opacity.toFixed(3)}" ` +
            `stroke-width="${sw.toFixed(2)}"/>`
        );
    }

    return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${width} ${height}" preserveAspectRatio="xMidYMid slice">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="${bgStart}"/>
      <stop offset="1" stop-color="${bgEnd}"/>
    </linearGradient>
    <radialGradient id="glow" cx="${originX}" cy="${originY}" r="${Math.round(R * 0.45)}" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="${glowColor}"/>
      <stop offset="1" stop-color="${glowColor.replace(/[\d.]+\)$/, '0)')}"/>
    </radialGradient>
  </defs>
  <rect width="${width}" height="${height}" fill="url(#bg)"/>
  <rect width="${width}" height="${height}" fill="url(#glow)"/>
  <g stroke="${strokeColor}" fill="none" stroke-linecap="round">
${paths.join('\n')}
  </g>
</svg>
`;
}

// ----------------------------------------------------------------------
// Desktop variant — 16:10. Origin sits just inside the lower-right
// corner; the fan sweeps from "almost straight up" round to "down-left".
// ----------------------------------------------------------------------
const desktop = generateSVG({
    width: 1600,
    height: 1000,
    originX: 1450,
    originY: 910,
    thetaMin: Math.PI * 0.08,
    thetaMax: Math.PI * 0.72,
    numCurves: 48,
});

// ----------------------------------------------------------------------
// Phone variant — 9:13. Slightly tighter fan because the canvas is
// taller-than-wide so the curves need to reach further upward.
// ----------------------------------------------------------------------
const phone = generateSVG({
    width: 900,
    height: 1300,
    originX: 790,
    originY: 1170,
    thetaMin: Math.PI * 0.04,
    thetaMax: Math.PI * 0.62,
    numCurves: 42,
});

const outDir = path.join(__dirname, '..', 'docs', 'img');
fs.mkdirSync(outDir, { recursive: true });
fs.writeFileSync(path.join(outDir, 'wallpaper-d.svg'), desktop);
fs.writeFileSync(path.join(outDir, 'wallpaper-p.svg'), phone);

console.log('Wrote:');
console.log('  docs/img/wallpaper-d.svg  (' + desktop.length + ' bytes)');
console.log('  docs/img/wallpaper-p.svg  (' + phone.length + ' bytes)');
