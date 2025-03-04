<template>
  <div>
    <section>
      <h1>{{ meta.user.username }}</h1>
      <p>
        <strong>Credentials:</strong> {{ meta.credentials.join(', ') }}
      </p>
      <p>
        <strong>Questions:</strong> {{ meta.questions.join(', ') }}
      </p>
      <p>
        <strong>Session Info:</strong> {{ meta.session_info }}
      </p>
      <p>
        <small class="text-muted">Last Updated: {{ meta.updated_at }}</small>
      </p>
    </section>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "SearchDetail",
  data() {
    return {
      meta: {
        user: { username: "" },
        credentials: [],
        questions: [],
        session_info: "",
        updated_at: ""
      }
    }
  },
  mounted() {
    // Retrieve the username from the route parameters
    const username = this.$route.params.username;
    // Replace `/api/search/detail/${username}` with your API endpoint URL.
    axios.get(`/api/search/detail/${username}`)
      .then(response => {
        this.meta = response.data;
      })
      .catch(error => {
        console.error('Error fetching search detail:', error);
      });
  }
}
</script>

<style scoped>
/* Add component-specific styles if needed */
</style>
