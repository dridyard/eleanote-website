// Eleanote Auth — handles all Cognito interactions for the website
//
// We talk to Cognito's REST API directly (no SDK needed — keeps the
// page lightweight). Tokens are stored in localStorage.
//
// Cognito User Pool: us-east-1_3KRHkFb46
// App Client: 7c1202jkhgdo3kdvunuvstm8ee

const COGNITO_REGION = 'us-east-1';
const COGNITO_POOL_ID = 'us-east-1_3KRHkFb46';
const COGNITO_CLIENT_ID = '7c1202jkhgdo3kdvunuvstm8ee';
const COGNITO_ENDPOINT = `https://cognito-idp.${COGNITO_REGION}.amazonaws.com/`;

// API base URL — Eleanote backend
const API_URL = 'https://feqbkbqpkc.execute-api.us-east-1.amazonaws.com/prod';

// Token storage keys in localStorage
const STORAGE = {
    ID_TOKEN: 'eleanote.idToken',
    ACCESS_TOKEN: 'eleanote.accessToken',
    REFRESH_TOKEN: 'eleanote.refreshToken',
    EMAIL: 'eleanote.email',
    EXPIRES_AT: 'eleanote.expiresAt',
};

// ----- Cognito API call helper -----
async function cognitoCall(operation, body) {
    const response = await fetch(COGNITO_ENDPOINT, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-amz-json-1.1',
            'X-Amz-Target': `AWSCognitoIdentityProviderService.${operation}`,
        },
        body: JSON.stringify(body),
    });

    const data = await response.json();
    if (!response.ok) {
        const error = new Error(data.message || 'Authentication error');
        error.code = data.__type || 'UnknownError';
        throw error;
    }
    return data;
}

// ----- Convert Cognito error codes into user-friendly messages -----
function friendlyError(err) {
    const code = err.code || '';
    const msg = err.message || '';

    if (code.includes('UsernameExistsException')) {
        return 'An account with this email already exists.';
    }
    if (code.includes('InvalidPasswordException')) {
        return 'Password must be at least 8 characters and include uppercase, lowercase, number, and a symbol.';
    }
    if (code.includes('InvalidParameterException')) {
        if (msg.toLowerCase().includes('password')) {
            return 'Password must be at least 8 characters and include uppercase, lowercase, number, and a symbol.';
        }
        if (msg.toLowerCase().includes('email')) {
            return 'Please enter a valid email address.';
        }
        return msg;
    }
    if (code.includes('NotAuthorizedException')) {
        if (msg.toLowerCase().includes('password attempts exceeded')) {
            return 'Too many failed attempts. Please try again in a few minutes.';
        }
        if (msg.toLowerCase().includes('disabled')) {
            return 'This account has been disabled. Contact support.';
        }
        return 'Email or password is incorrect.';
    }
    if (code.includes('UserNotFoundException')) {
        return 'Email or password is incorrect.';
    }
    if (code.includes('UserNotConfirmedException')) {
        return 'Please verify your email first. Check your inbox for the verification code.';
    }
    if (code.includes('CodeMismatchException')) {
        return 'That code is incorrect. Please check your email and try again.';
    }
    if (code.includes('ExpiredCodeException')) {
        return 'That code has expired. Please request a new one.';
    }
    if (code.includes('LimitExceededException')) {
        return 'Too many requests. Please wait a few minutes and try again.';
    }
    if (code.includes('TooManyRequestsException')) {
        return 'Too many requests. Please slow down and try again.';
    }
    if (code.includes('PasswordResetRequiredException')) {
        return 'Your password needs to be reset. Click "Forgot password" below.';
    }
    return msg || 'Something went wrong. Please try again.';
}

// ----- Sign Up -----
async function signUp(email, password) {
    return cognitoCall('SignUp', {
        ClientId: COGNITO_CLIENT_ID,
        Username: email,
        Password: password,
        UserAttributes: [
            { Name: 'email', Value: email },
        ],
    });
}

// ----- Confirm sign-up with email code -----
async function confirmSignUp(email, code) {
    return cognitoCall('ConfirmSignUp', {
        ClientId: COGNITO_CLIENT_ID,
        Username: email,
        ConfirmationCode: code,
    });
}

// ----- Resend verification code -----
async function resendCode(email) {
    return cognitoCall('ResendConfirmationCode', {
        ClientId: COGNITO_CLIENT_ID,
        Username: email,
    });
}

// ----- Sign In -----
async function signIn(email, password) {
    const result = await cognitoCall('InitiateAuth', {
        AuthFlow: 'USER_PASSWORD_AUTH',
        ClientId: COGNITO_CLIENT_ID,
        AuthParameters: {
            USERNAME: email,
            PASSWORD: password,
        },
    });
    return result;
}

// ----- Respond to MFA challenge with code -----
async function respondToMfaChallenge(email, code, session) {
    return cognitoCall('RespondToAuthChallenge', {
        ClientId: COGNITO_CLIENT_ID,
        ChallengeName: 'EMAIL_OTP',
        Session: session,
        ChallengeResponses: {
            USERNAME: email,
            EMAIL_OTP_CODE: code,
        },
    });
}

// ----- Forgot password (start) -----
async function forgotPassword(email) {
    return cognitoCall('ForgotPassword', {
        ClientId: COGNITO_CLIENT_ID,
        Username: email,
    });
}

// ----- Confirm forgot password (with code + new password) -----
async function confirmForgotPassword(email, code, newPassword) {
    return cognitoCall('ConfirmForgotPassword', {
        ClientId: COGNITO_CLIENT_ID,
        Username: email,
        ConfirmationCode: code,
        Password: newPassword,
    });
}

// ----- Sign out (clears local tokens; optionally invalidates server-side too) -----
async function signOut() {
    const accessToken = localStorage.getItem(STORAGE.ACCESS_TOKEN);
    if (accessToken) {
        try {
            await cognitoCall('GlobalSignOut', { AccessToken: accessToken });
        } catch (e) {
            // Even if server signout fails, we still clear local state
            console.warn('Server signout failed, clearing local tokens anyway');
        }
    }
    Object.values(STORAGE).forEach(k => localStorage.removeItem(k));
}

// ----- Save tokens after successful login -----
function saveTokens(authResult, email) {
    localStorage.setItem(STORAGE.ID_TOKEN, authResult.IdToken);
    localStorage.setItem(STORAGE.ACCESS_TOKEN, authResult.AccessToken);
    if (authResult.RefreshToken) {
        localStorage.setItem(STORAGE.REFRESH_TOKEN, authResult.RefreshToken);
    }
    localStorage.setItem(STORAGE.EMAIL, email);
    // ID/Access tokens are good for 60 minutes
    localStorage.setItem(STORAGE.EXPIRES_AT, String(Date.now() + 60 * 60 * 1000));
}

// ----- Check if currently logged in -----
function isLoggedIn() {
    const idToken = localStorage.getItem(STORAGE.ID_TOKEN);
    const expiresAt = parseInt(localStorage.getItem(STORAGE.EXPIRES_AT) || '0', 10);
    return !!idToken && Date.now() < expiresAt;
}

function getStoredEmail() {
    return localStorage.getItem(STORAGE.EMAIL) || '';
}

// ----- UI helpers -----
function showAlert(elementId, type, message) {
    const el = document.getElementById(elementId);
    if (!el) return;
    el.className = `alert alert-${type} show`;
    el.textContent = message;
}

function hideAlert(elementId) {
    const el = document.getElementById(elementId);
    if (el) el.className = 'alert';
}

function setButtonLoading(btn, loading) {
    if (loading) {
        btn.disabled = true;
        btn.dataset.originalText = btn.innerHTML;
        btn.innerHTML = '<span class="spinner"></span><span>Working&hellip;</span>';
    } else {
        btn.disabled = false;
        if (btn.dataset.originalText) {
            btn.innerHTML = btn.dataset.originalText;
        }
    }
}

// Pull a query string parameter
function getParam(name) {
    const url = new URL(window.location.href);
    return url.searchParams.get(name) || '';
}

// ----- API helpers (for calls to our server endpoints) -----
async function apiCall(path, options = {}) {
    const idToken = localStorage.getItem(STORAGE.ID_TOKEN);
    if (!idToken) throw new Error('Not signed in');

    const response = await fetch(API_URL + path, {
        ...options,
        headers: {
            'Authorization': 'Bearer ' + idToken,
            'Content-Type': 'application/json',
            ...(options.headers || {}),
        },
    });

    let data;
    try { data = await response.json(); } catch { data = null; }

    if (!response.ok) {
        const err = new Error((data && data.error) || `Request failed (${response.status})`);
        err.status = response.status;
        throw err;
    }
    return data;
}

async function getProfile() {
    return apiCall('/profile', { method: 'GET' });
}

async function updateProfile(updates) {
    return apiCall('/profile', {
        method: 'PATCH',
        body: JSON.stringify(updates),
    });
}

// ----- Required agreement versions -----
// These MUST match the server's REQUIRED_*_VERSION env vars on the
// /download-url endpoint. When a legal document is revised, bump the version
// both here and on the server; users will then be required to re-accept.
const REQUIRED_AGREEMENTS = { terms: '1.1', privacy: '0.1', baa: '0.1' };

// True only if the profile has accepted the CURRENT version of all three docs.
function agreementsAccepted(profile) {
    return !!profile
        && profile.termsAcceptedVersion === REQUIRED_AGREEMENTS.terms
        && profile.privacyAcceptedVersion === REQUIRED_AGREEMENTS.privacy
        && profile.baaAcceptedVersion === REQUIRED_AGREEMENTS.baa;
}

// True only if the user has finished onboarding: provided their name AND
// accepted the current agreements. This is the gate for reaching the dashboard
// and downloading. The server enforces the same rule on /download-url.
function onboardingComplete(profile) {
    return !!profile
        && !!(profile.firstName && profile.firstName.trim())
        && !!(profile.lastName && profile.lastName.trim())
        && agreementsAccepted(profile);
}

// Expose everything as a namespace so the page scripts can use it
window.EleanoteAuth = {
    signUp,
    confirmSignUp,
    resendCode,
    signIn,
    respondToMfaChallenge,
    forgotPassword,
    confirmForgotPassword,
    signOut,
    saveTokens,
    isLoggedIn,
    getStoredEmail,
    friendlyError,
    showAlert,
    hideAlert,
    setButtonLoading,
    getParam,
    getProfile,
    updateProfile,
    apiCall,
    REQUIRED_AGREEMENTS,
    agreementsAccepted,
    onboardingComplete,
    STORAGE,
};
