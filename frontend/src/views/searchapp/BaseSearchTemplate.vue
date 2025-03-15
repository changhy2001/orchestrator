<!-- BaseSearchTemplate.vue -->
<template>
  <div>
    <h2><slot name="title">Search</slot></h2>
    
    <!-- Search Form -->
    <form @submit.prevent="performSearch">
      <!-- Use a slot to allow custom search fields -->
      <slot name="search-form" :query="query"></slot>
      <button type="submit" class="btn btn-primary btn-block">Search</button>
    </form>
    
    <!-- Search Results -->
    <div v-if="results.length > 0">
      <div class="small-break"></div>
      <p>Results: {{ results.length }}</p>
      <div class="small-break"></div>
      <table class="table custom-table">
        <thead>
          <tr>
            <slot name="table-header"></slot>
          </tr>
        </thead>
        <tbody>
          <slot name="table-body" :results="results"></slot>
        </tbody>
      </table>
    </div>
    <div v-else>
      <p>No results found.</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "BaseSearchTemplate",
  props: {
    // The API endpoint that child components can override
    apiEndpoint: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      // The default query object—child components can extend it
      query: {
        q: "",
        username_contains: "",
        credentials_contains: "",
        questions_contains: "",
        session_info_contains: "",
        created_at_min: "",
        created_at_max: "",
        updated_at_min: "",
        updated_at_max: "",
      },
      results: [],
    };
  },
  mounted() {
    // Populate query from route params if needed, then perform search
    Object.assign(this.query, this.$route.query);
    this.performSearch();
  },
  methods: {
    performSearch() {
      axios
        .get(this.apiEndpoint, { params: this.query })
        .then((response) => {
          this.results = response.data;
          this.$router.push({ query: this.query });
        })
        .catch((error) => {
          console.error("Error during search:", error);
        });
    },
  },
};
</script>

<style scoped>
.small-break {
  margin: 10px;
}
</style>
