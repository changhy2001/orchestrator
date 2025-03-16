<!-- BaseSearchTemplate.vue -->
<template>
  <div>
    <h2><slot name="title">Search</slot></h2>

    <!-- Search Form -->
    <form @submit.prevent="performSearch">
      <slot name="search-form" :query="query"></slot>
      <button type="submit" class="btn btn-primary btn-block">Search</button>
    </form>

    <!-- Add Form -->
    <div v-if="showAddForm" class="add-form">
      <form @submit.prevent="handleSubmitAdd">
        <slot name="add-form" :form="form"></slot>
        <button type="submit" class="btn btn-success">Submit</button>
      </form>
    </div>

    <!-- Results and Add Button -->
    <div v-if="results.length > 0">
      <div class="small-break"></div>
      <div class="results-header">
        <p class="results-text">Results: {{ results.length }}</p>
        <button class="btn btn-success" @click="handleAdd">Add</button>
      </div>
      <div class="small-break"></div>
      <table class="table custom-table">
        <thead>
          <tr>
            <!-- Main header columns -->
            <slot name="table-header"></slot>
            <!-- Actions column (only if enabled) -->
            <th v-if="enableActions">Actions</th>
          </tr>
        </thead>
        <tbody>
          <template v-for="(row) in results" :key="row.id">
            <tr>
              <slot name="table-body" :row="row"></slot>
              <!-- Default Actions cell (only if enabled) -->
              <td v-if="enableActions" class="actions-cell">
                <button class="btn" @click="handleEdit(row)">Edit</button>
                <button class="btn" @click="handleDelete(row)">Delete</button>
              </td>
            </tr>
          </template>
        </tbody>
      </table>
    </div>
    <div v-else>
      <p>No results found.</p>
      <!-- If there are no results, you might still want to show the Add button -->
      <div class="small-break"></div>
      <div class="results-header">
        <p class="results-text">Results: 0</p>
        <button class="btn btn-success" @click="handleAdd">Add</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { getCookie } from '@/utils/cookie';

export default {
  name: "BaseSearchTemplate",
  props: {
    apiEndpoint: {
      type: String,
      required: true,
    },
    // Enable or disable the actions column
    enableActions: {
      type: Boolean,
      default: true,
    },
    // Optionally specify an edit route name to automatically navigate on edit
    editRouteName: {
      type: String,
      default: "",
    },
  },
  data() {
    return {
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
      showAddForm: false, // Controls visibility of the add form
      form: {
        user: "",
        questions: "",
        credentials: "",
        session_info: "",
        user_logs: "",
      },
    };
  },
  mounted() {
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
    handleEdit(row) {
      if (this.editRouteName) {
        this.$router.push({ name: this.editRouteName, params: { pk: row.id } });
      } else {
        console.log("Edit action for row:", row);
      }
    },
    handleDelete(row) {
      if (confirm(`Are you sure you want to delete this record?`)) {
        const csrfToken = getCookie("csrftoken");
        axios.delete(`${this.apiEndpoint}/${row.id}/`, {
          headers: {
            "X-CSRFToken": csrfToken
          }
        })
        .then(() => {
          alert("Record deleted successfully");
          this.performSearch();
        })
        .catch((error) => {
          console.error("Error deleting record:", error);
          alert("Error deleting record.");
        });
      }
    },
    handleAdd() {
      // Show the add form when the Add button is clicked
      this.showAddForm = true;
      this.$emit("add-row");
    },
    handleSubmitAdd() {
      // Retrieve CSRF token if needed (for session authentication)
      const csrfToken = getCookie("csrftoken");

      axios
        .post(this.apiEndpoint + "/", this.form, {
        headers: {
            "X-CSRFToken": csrfToken,
          },
        })
        .then(response => {
        // Emit a success event with the response data.
        this.$emit("formSubmitted", response.data);
        })
        .catch(error => {
        console.error("Error submitting form:", error);
        this.error =
            error.response && error.response.data
            ? error.response.data
            : error.message;
        this.$emit("formError", this.error);
        this.showAddForm = false;
        });
    },
  },
};
</script>

<style scoped>
.small-break {
  margin: 10px;
}

/* Flex container for results header */
.results-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

/* Style for results text */
.results-text {
  margin: 0;
}

/* Optional: spacing between buttons in the actions cell */
.actions-cell button + button {
  margin-left: 0.7rem;
}

/* Center the actions cell content */
.actions-cell {
  text-align: center;
}

/* Optional styling for the add form */
.add-form {
  margin: 15px 0;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}
</style>
