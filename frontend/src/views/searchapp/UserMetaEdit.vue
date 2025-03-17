<template>
  <div class="user-meta-edit">
    <BaseFormTemplate
      :initialForm="form"
      @submit="handleUpdate"
      @cancel="handleCancel"
    >
      <template #title>
        Edit UserMeta
      </template>
      <template #form="{ form }">
        <div class="form-group">
          <label class="small-label" for="username">Username</label>
          <input
            id="username"
            v-model="form.username"
            class="form-control"
            placeholder="Enter username"
            type="text"
            required
          />
        </div>

        <div class="form-group">
          <label class="small-label" for="questions">Questions (comma-separated)</label>
          <textarea
            id="questions"
            v-model="form.questions"
            class="form-control"
            placeholder="Enter questions, separated by commas"
          ></textarea>
        </div>

        <div class="form-group">
          <label class="small-label" for="credentials">Credentials (comma-separated)</label>
          <textarea
            id="credentials"
            v-model="form.credentials"
            class="form-control"
            placeholder="Enter credentials, separated by commas"
          ></textarea>
        </div>

        <div class="form-group">
          <label class="small-label" for="session_info">Session Info</label>
          <textarea
            id="session_info"
            v-model="form.session_info"
            class="form-control"
            placeholder="Enter session info"
          ></textarea>
        </div>

        <div class="form-group">
          <label class="small-label" for="user_logs">User Logs (comma-separated)</label>
          <textarea
            id="user_logs"
            v-model="form.user_logs"
            class="form-control"
            placeholder="Enter user logs, separated by commas"
          ></textarea>
        </div>
      </template>
    </BaseFormTemplate>
  </div>
</template>

<script>
import axios from "axios";
import { getCookie } from '@/utils/cookie';
import BaseFormTemplate from "@/views/searchapp/BaseFormTemplate.vue";

export default {
  name: "UserMetaEdit",
  components: {
    BaseFormTemplate,
  },
  data() {
    return {
      // The form object is used to pre-populate the fields.
      form: {
        username: "",
        questions: "",
        credentials: "",
        session_info: "",
        user_logs: "",
      },
      error: null,
    };
  },
  mounted() {
    const id = this.$route.params.id;  // use "id"
    console.log("Fetched id from route:", id);
    if (!id) {
      this.error = "Missing route parameter: id";
      return;
    }
    this.fetchUserMeta(id);
  },
  methods: {
    fetchUserMeta(id) {
      axios
        .get(`/searchapp/usermeta/${id}/`)
        .then((response) => {
          const data = response.data;
          this.form.username = data.username;
          this.form.questions = Array.isArray(data.questions)
            ? data.questions.join(", ")
            : data.questions;
          this.form.credentials = Array.isArray(data.credentials)
            ? data.credentials.join(", ")
            : data.credentials;
          this.form.session_info = data.session_info;
          this.form.user_logs = Array.isArray(data.user_logs)
            ? data.user_logs.join(", ")
            : data.user_logs;
        })
        .catch((error) => {
          console.error("Error fetching usermeta:", error);
          this.error = "Failed to load usermeta.";
        });
    },
    handleUpdate(updatedForm) {
      const id = this.$route.params.id; // use "id"
      const csrfToken = getCookie("csrftoken");
      const payload = {
        username: updatedForm.username,
        questions: updatedForm.questions
          ? updatedForm.questions.split(",").map(q => q.trim()).filter(q => q !== "")
          : [],
        credentials: updatedForm.credentials
          ? updatedForm.credentials.split(",").map(c => c.trim()).filter(c => c !== "")
          : [],
        session_info: updatedForm.session_info,
        user_logs: updatedForm.user_logs
          ? updatedForm.user_logs.split(",").map(l => l.trim()).filter(l => l !== "")
          : [],
      };

      axios
        .patch(`/searchapp/usermeta/${id}/`, payload, {
          headers: { "X-CSRFToken": csrfToken },
        })
        .then((response) => {
          // Navigate back to the list view (or wherever is appropriate)
          this.$router.push({ name: "UserMetaList" });
        })
        .catch((error) => {
          console.error("Error updating usermeta:", error);
          this.error = "Failed to update record.";
        });
    },
    handleCancel() {
      this.$router.push({ name: "UserMetaList" });
    },
  }

};
</script>

<style scoped>
.user-meta-edit {
  max-width: 600px;
  margin: 20px auto;
  padding: 10px;
}
</style>
