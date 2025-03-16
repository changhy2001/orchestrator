<!-- BaseDetailTemplate.vue -->
<template>
  <div>
    <!-- Show error message if there's an error -->
    <div v-if="error">
      <p>Error loading details: {{ error }}</p>
    </div>
    <!-- When data is available, pass it to the default slot -->
    <div v-else-if="meta">
      <slot :meta="meta"></slot>
    </div>
    <!-- Loading state -->
    <div v-else>
      <p>Loading details...</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "BaseDetailTemplate",
  props: {
    // Base API endpoint, e.g. "/search"
    apiEndpoint: {
      type: String,
      required: true,
    },
    // The name of the route parameter to use (e.g., "username")
    paramName: {
      type: String,
      default: "id",
    },
  },
  data() {
    return {
      meta: null,
      error: null,
    };
  },
  mounted() {
    // Retrieve the parameter value from the route
    const paramValue = this.$route.params[this.paramName];
    // Construct the URL: for example, "/search/<username>/"
    axios
      .get(`${this.apiEndpoint}/${paramValue}/`)
      .then((response) => {
        this.meta = response.data;
      })
      .catch((error) => {
        console.error("Error fetching detail:", error);
        this.error =
          error.response && error.response.data
            ? error.response.data
            : error.message;
      });
  },
};
</script>

<style scoped>
/* Optional styles for your detail page */
</style>
  