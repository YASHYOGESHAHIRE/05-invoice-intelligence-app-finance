
const API_BASE =
  'http://127.0.0.1:8000/auth';


const Auth = {

  /* =========================
     LOGIN
  ========================= */

  async login(credentials) {

    const response = await fetch(
      `${API_BASE}/login`,
      {
        method: 'POST',

        headers: {
          'Content-Type': 'application/json'
        },

        body: JSON.stringify(credentials)
      }
    );

    const data =
      await response.json();

    if (!response.ok) {

      throw new Error(
        data.detail || 'Login failed'
      );
    }

    this.setSession(data);

    return data;
  },


  /* =========================
     SIGNUP
  ========================= */

  async signup(userData) {

    const response = await fetch(
      `${API_BASE}/signup`,
      {
        method: 'POST',

        headers: {
          'Content-Type': 'application/json'
        },

        body: JSON.stringify(userData)
      }
    );

    const data =
      await response.json();

    if (!response.ok) {

      throw new Error(
        data.detail || 'Signup failed'
      );
    }

    this.setSession(data);

    return data;
  },


  /* =========================
     SESSION
  ========================= */

  setSession(data) {

    localStorage.setItem(
      'token',
      data.access_token
    );

    localStorage.setItem(
      'user',
      JSON.stringify(data.user)
    );
  },


  clearSession() {

    localStorage.removeItem('token');

    localStorage.removeItem('user');
  },


  /* =========================
     USER
  ========================= */

  getToken() {

    return localStorage.getItem(
      'token'
    );
  },


  getUser() {

    return JSON.parse(
      localStorage.getItem('user')
    );
  },


  isLoggedIn() {

    return !!this.getToken();
  },


  /* =========================
     LOGOUT
  ========================= */

  logout() {

    this.clearSession();

    window.location.href =
      'login.html';
  },


  /* =========================
     ROUTE PROTECTION
  ========================= */

  protectRoute() {

    const params =
      new URLSearchParams(
        window.location.search
      );

    const tokenFromGoogle =
      params.get('token');

    /*
      Google OAuth Redirect
    */

    if (tokenFromGoogle) {

      localStorage.setItem(
        'token',
        tokenFromGoogle
      );

      /*
        Remove token from URL
      */

      window.history.replaceState(
        {},
        document.title,
        window.location.pathname
      );
    }

    /*
      Not logged in
    */

    if (!this.isLoggedIn()) {

      window.location.href =
        'login.html';
    }
  },


  /* =========================
     REDIRECT IF LOGGED IN
  ========================= */

  redirectIfAuthenticated() {

    if (this.isLoggedIn()) {

      window.location.href =
        'main.html';
    }
  },


  /* =========================
     GOOGLE LOGIN
  ========================= */

  googleLogin() {

    window.location.href =
      `${API_BASE}/google/login`;
  },


  /* =========================
     LOAD USER INTO UI
  ========================= */

  loadUser(elementId = 'userName') {

    const user = this.getUser();

    if (!user) return;

    const element =
      document.getElementById(elementId);

    if (element) {

      element.innerText =
        user.name || user.email;
    }
  }
};

