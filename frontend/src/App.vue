<template>
  <div id="app">
    <nav>
      <!-- Navigation using Vue Router -->
      <router-link to="/" class="nav-button" aria-label="Home" title="Home">Home</router-link>
      <router-link to="/about" class="nav-button" aria-label="About" title="About">About</router-link>
      <!-- Render based on authentication state -->
      <template v-if="isAuthenticated">
        <router-link to="/searchapp" class="nav-button" aria-label="AppHome" title="AppHome">Search App</router-link>
        <button @click="handleLogout" class="nav-button" aria-label="Logout" title="Logout">Logout</button>
      </template>
      <template v-else>
        <router-link to="/register" class="nav-button" aria-label="Register" title="Register">Register</router-link>
        <router-link to="/login" class="nav-button" aria-label="Login" title="Login">Login</router-link>
      </template>
    </nav>
    <main>
      <router-view />
    </main>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'App',
  computed: {
    ...mapGetters(['isAuthenticated', 'user'])
  },
  methods: {
    ...mapActions(['logout']),
    async handleLogout() {
      const success = await this.logout();
      if (success) {
        this.$router.push({ name: 'Home' });
      }
    }
  }
};
</script>

<style>
@import "@/assets/css/style.css";

</style>
