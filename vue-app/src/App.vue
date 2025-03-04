<template>
  <div id="app">
    <nav>
      <!-- Using Vue Router links -->
      <router-link to="/" aria-label="Home" title="Home">🏠</router-link> | 
      <router-link to="/about" aria-label="About" title="About">🗒️</router-link> | 
      <!-- Replace authentication logic with Vue data or state management if needed -->
      <template v-if="userIsAuthenticated">
        <router-link to="/search" aria-label="Search" title="Search">🔍</router-link> | 
        <!-- Simulate a logout button -->
        <button @click="logout" class="logout-button" aria-label="User Logout" title="User Logout">👋</button>
      </template>
      <template v-else>
        <router-link to="/register" aria-label="User Registration" title="User Registration">🔏</router-link> | 
        <router-link to="/login" aria-label="User Login" title="User Login">🔐</router-link>
      </template>
    </nav>
    <main>
      <!-- Route outlet: this is where your Home, About, etc. pages will display -->
      <router-view />
    </main>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      // Replace with proper authentication check
      userIsAuthenticated: false,
    };
  },
  methods: {
    logout() {
      // Implement logout logic as needed
      this.userIsAuthenticated = false;
      console.log("User logged out");
    },
  },
};
</script>

<style>
/* Global styles or import your CSS file here */
@import "@/assets/css/style.css";
</style>
