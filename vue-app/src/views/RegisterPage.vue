<template>
  <div>
    <h1>Register a New User</h1>
    <form class="form-with-validation" @submit.prevent="submitRegister">
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
        <label for="email">Email:</label>
        <input 
          type="email" 
          id="email" 
          v-model="form.email" 
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
      <button type="submit" class="form-submit">Register</button>
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
        email: '',
        password: ''
      }
    };
  },
  methods: {
    submitRegister() {
        axios.post('/users/api/register/', this.form)
            .then(response => {
            if (response.data.success) {
                console.log('Registration successful:', response.data.message);
                // e.g., redirect or store auth state
                this.$router.push({ name: 'Search' });
            } else {
                console.error('Registration errors:', response.data.errors);
            }
            })
            .catch(error => {
            console.error('Registration error:', error);
            });
        }
  }
};
</script>

<style scoped>
/* Component-specific styles can be added here, or rely on your global CSS */
</style>
