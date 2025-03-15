<template>
  <div>
    <h1>Register a New User</h1>
    <!-- Display error message if present -->
    <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
    
    <form class="form-with-validation" @submit.prevent="submitRegister">
      <!-- Username Field -->
      <div class="form-group">
        <label for="username">Username:</label>
        <p class="helptext">
          Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
        </p>
        <input
          type="text"
          id="username"
          v-model="form.username"
          required
          class="form-control"
        />
      </div>

      <!-- Password Field -->
      <div class="form-group">
        <label for="password">Password:</label>
        <p class="helptext">
          Your password can't be too similar to your other personal information.<br />
          Your password must contain at least 8 characters.<br />
          Your password can't be a commonly used password.<br />
          Your password can't be entirely numeric.
        </p>
        <input
          type="password"
          id="password"
          v-model="form.password"
          required
          class="form-control"
        />
      </div>

      <!-- Password Confirmation Field -->
      <div class="form-group">
        <label for="confirmPassword">Password confirmation:</label>
        <p class="helptext">
          Enter the same password as before, for verification.
        </p>
        <input
          type="password"
          id="confirmPassword"
          v-model="form.confirmPassword"
          required
          class="form-control"
        />
      </div>

      <!-- Submit Button -->
      <button type="submit" class="form-submit">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'RegisterPage',
  data() {
    return {
      form: {
        username: '',
        password: '',
        confirmPassword: ''
      },
      errorMessage: ''  // Holds a single error message
    };
  },
  methods: {
    async submitRegister() {
      // Clear any previous error message
      this.errorMessage = '';

      // Basic client-side check to ensure passwords match
      if (this.form.password !== this.form.confirmPassword) {
        this.errorMessage = 'Passwords do not match.';
        return;
      }

      // Prepare data for the API to match UserCreationForm fields
      const requestData = {
        username: this.form.username,
        password1: this.form.password,
        password2: this.form.confirmPassword
      };

      try {
        const response = await axios.post('/users/register/', requestData);
        if (response.data.success) {
          await this.$store.dispatch('checkAuthStatus');
          this.$router.push({ name: 'SearchApp' });
        } else {
          // Set a fixed error message if registration fails
          this.errorMessage = 'Registration unsuccessful. Please check your input.';
        }
      } catch (error) {
        this.errorMessage = 'Registration unsuccessful. Please try again.';
      }
    }
  }
};
</script>

<style scoped>

</style>
