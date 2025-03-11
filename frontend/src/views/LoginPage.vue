<template>
  <div>
    <h1>User Login</h1>
    <!-- Display error message if present -->
    <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
    
    <!-- The form submission is handled by the submitLogin method -->
    <form class="form-with-validation" @submit.prevent="submitLogin">
      <div class="form-group">
        <label for="username">Username:</label>
        <input 
          type="text" 
          id="username" 
          v-model="form.username" 
          required 
          class="form-control"
        />
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input 
          type="password" 
          id="password" 
          v-model="form.password" 
          required 
          class="form-control"
        />
      </div>
      <button type="submit" class="form-submit">Login</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LoginPage',
  data() {
    return {
      form: {
        username: '',
        password: '',
      },
      errorMessage: '' // Holds a single error message
    };
  },
  methods: {
    async submitLogin() {
      // Clear any previous error messages
      this.errorMessage = '';
      try {
        const response = await axios.post('/users/login/', this.form);
        if (response.data.success) {
          await this.$store.dispatch('checkAuthStatus');
          this.$router.push({ name: 'Search' });
        } else {
          // Set a fixed error message
          this.errorMessage = 'Invalid username or password.';
        }
      } catch (error) {
        // Fallback error message
        this.errorMessage = 'Invalid username or password.';
      }
    }
  }
};
</script>

<style scoped>
/* Component-specific styles can be added here, or rely on your global CSS */
</style>
