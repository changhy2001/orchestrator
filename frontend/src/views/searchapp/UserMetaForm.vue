<template>
    <div class="user-meta-form">
      <BaseFormTemplate
        :apiEndpoint="apiEndpoint"
        :initialForm="initialForm"
        @formSubmitted="handleSuccess"
        @formError="handleError"
      >
        <template #title>
          Create UserMeta
        </template>
        <template #form-fields="{ form, updateForm }">
          <div class="form-group">
            <label for="user_username">Username:</label>
            <input
              id="user_username"
              type="text"
              v-model="form.user_username"
              @input="updateForm('user_username', $event.target.value)"
              required
            />
          </div>
          <div class="form-group">
            <label for="credentials">Credentials (comma separated):</label>
            <input
              id="credentials"
              type="text"
              v-model="form.credentials"
              @input="updateForm('credentials', $event.target.value)"
            />
          </div>
          <div class="form-group">
            <label for="questions">Questions (comma separated):</label>
            <input
              id="questions"
              type="text"
              v-model="form.questions"
              @input="updateForm('questions', $event.target.value)"
            />
          </div>
          <div class="form-group">
            <label for="session_info">Session Info:</label>
            <textarea
              id="session_info"
              v-model="form.session_info"
              @input="updateForm('session_info', $event.target.value)"
            ></textarea>
          </div>
        </template>
      </BaseFormTemplate>
    </div>
  </template>
  
  <script>
  export default {
    name: "UserMetaForm",
    data() {
      return {
        apiEndpoint: "/searchapp/usermeta",
        initialForm: {
          user_username: "",
          credentials: "",
          questions: "",
          session_info: "",
        },
      };
    },
    methods: {
      // Process the submitted form data if needed before navigation
      handleSuccess(responseData) {
        alert("UserMeta created successfully!");
        // Optionally, process responseData or redirect to another page:
        this.$router.push({ name: "UserMetaList" });
      },
      handleError(errorMessage) {
        alert("Error creating UserMeta: " + errorMessage);
      },
    },
  };
  </script>
  
  <style scoped>
  .user-meta-form {
    max-width: 600px;
    margin: auto;
    padding: 20px;
  }
  .form-group {
    margin-bottom: 15px;
  }
  label {
    display: block;
    font-weight: bold;
    margin-bottom: 5px;
  }
  input,
  textarea {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
  }
  </style>
  