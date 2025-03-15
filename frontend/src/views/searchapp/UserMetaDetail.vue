<!-- UserMetaDetail.vue -->
<template>
  <BaseDetailTemplate apiEndpoint="/searchapp/usermeta" paramName="username">
    <!-- The default slot receives the fetched data as 'meta' -->
    <template #default="{ meta }">
      <section>
        <h1>{{ meta.user_username }}</h1>
        <p>
          <strong>Credentials:</strong>
          <!-- Display credentials (adjust formatting as needed) -->
          {{ meta.credentials }}
        </p>
        <p>
          <strong>Questions:</strong>
          {{ meta.questions }}
        </p>
        <p>
          <strong>Session Info:</strong>
          {{ meta.session_info }}
        </p>
        <p>
          <small class="text-muted">Last Updated: {{ meta.updated_at }}</small>
        </p>
      </section>
    </template>
  </BaseDetailTemplate>
</template>

<script>
import BaseDetailTemplate from "@/views/searchapp/BaseDetailTemplate.vue";

export default {
  name: "UserMetaDetail",
  components: {
    BaseDetailTemplate,
  },
};
</script>

<style scoped>
/* Add component-specific styles as needed */
</style>
