<!-- UserMeta.vue -->
<template>
  <BaseSearchTemplate
    ref="baseSearch"
    apiEndpoint="/searchapp/usermeta"
    editRouteName="UserMetaEdit"
    @add-row="handleAdd"
    @formSubmitted="handleFormSubmitted"
    @formError="handleFormError"
  >
    <!-- Title -->
    <template #title>
      Search Users
    </template>

    <!-- Search Form -->
    <template #search-form="{ query }">
      <div class="form-row">
        <div class="form-group col-12">
          <div class="input-group">
            <input
              type="search"
              class="form-control py-2 border-right-0 border"
              v-model="query.q"
              placeholder="Search users or questions..."
            />
          </div>
        </div>
      </div>
      <!-- Additional filters -->
      <div class="form-row">
        <div class="form-group col-md-3">
          <input type="text" class="form-control" v-model="query.username_contains" placeholder="Username contains...">
        </div>
        <div class="form-group col-md-3">
          <input type="text" class="form-control" v-model="query.credentials_contains" placeholder="User credentials...">
        </div>
        <div class="form-group col-md-3">
          <input type="text" class="form-control" v-model="query.questions_contains" placeholder="Question contains...">
        </div>
        <div class="form-group col-md-3">
          <input type="text" class="form-control" v-model="query.session_info_contains" placeholder="Session info contains...">
        </div>
      </div>
      <!-- Date filters -->
      <div class="form-row">
        <div class="form-group col-md-3">
          <label class="small-label">Created At (Min)</label>
          <input type="date" class="form-control" v-model="query.created_at_min">
        </div>
        <div class="form-group col-md-3">
          <label class="small-label">Created At (Max)</label>
          <input type="date" class="form-control" v-model="query.created_at_max">
        </div>
        <div class="form-group col-md-3">
          <label class="small-label">Updated At (Min)</label>
          <input type="date" class="form-control" v-model="query.updated_at_min">
        </div>
        <div class="form-group col-md-3">
          <label class="small-label">Updated At (Max)</label>
          <input type="date" class="form-control" v-model="query.updated_at_max">
        </div>
      </div>
    </template>

    <!-- Add Form Slot -->
    <template #add-form="{ form }">
      <div class="form-group">
        <label class="small-label" for="user">User</label>
        <select id="user" name="user" v-model="form.user" class="form-control">
          <option disabled value="">Select a user</option>
          <option v-for="u in users" :key="u.id" :value="u.id">
            {{ u.username }}
          </option>
        </select>
      </div>
      <div class="form-group">
        <label class="small-label" for="questions">Questions (comma-separated)</label>
        <textarea
          id="questions"
          name="questions"
          v-model="form.questions"
          class="form-control"
          placeholder="Enter questions, separated by commas"
          autocomplete="off"
        ></textarea>
      </div>
      <div class="form-group">
        <label class="small-label" for="credentials">Credentials (JSON format)</label>
        <textarea
          id="credentials"
          name="credentials"
          v-model="form.credentials"
          class="form-control"
          placeholder='Enter credentials in JSON format'
          autocomplete="off"
        ></textarea>
      </div>
      <div class="form-group">
        <label class="small-label" for="session_info">Session Info</label>
        <textarea
          id="session_info"
          name="session_info"
          v-model="form.session_info"
          class="form-control"
          placeholder="Enter session info"
          autocomplete="off"
        ></textarea>
      </div>
      <div class="form-group">
        <label class="small-label" for="user_logs">User Logs (JSON format)</label>
        <textarea
          id="user_logs"
          name="user_logs"
          v-model="form.user_logs"
          class="form-control"
          placeholder='Enter user logs in JSON format'
          autocomplete="off"
        ></textarea>
      </div>
    </template>

    <!-- Table Header -->
    <template #table-header>
      <th>ID</th>
      <th>User</th>
      <th>Credentials</th>
      <th>Questions</th>
      <th>Session Info</th>
      <th>Created At</th>
      <th>Last Updated</th>
    </template>

    <!-- Table Body -->
    <template #table-body="{ row }">
      <td>
        <router-link :to="{ name: 'UserMetaDetail', params: { pk: row.id } }">
          {{ row.id }}
        </router-link>
      </td>
      <td>{{ row.username }}</td>
      <td>{{ row.credentials }}</td>
      <td>{{ row.questions }}</td>
      <td>{{ row.session_info }}</td>
      <td>{{ row.created_at }}</td>
      <td>{{ row.updated_at }}</td>
    </template>
  </BaseSearchTemplate>
</template>

<script>
import BaseSearchTemplate from '@/views/searchapp/BaseSearchTemplate.vue';

export default {
  name: "UserMeta",
  components: {
    BaseSearchTemplate,
  },
  methods: {
    handleFormSubmitted(formData) {
      // Handle successful submission (e.g., refresh list, show message)
      console.log("Form submitted successfully:", formData);
    },
    handleFormError(error) {
      // Handle errors (e.g., display error message)
      console.error("Form submission error:", error);
    },
    handleAdd() {
      // Additional handling when the Add button is clicked if needed.
      console.log("Add button clicked");
    },
  },
};
</script>
