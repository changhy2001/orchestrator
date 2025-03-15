<!-- UserMeta.vue -->
<template>
  <BaseSearchTemplate apiEndpoint="/searchapp/usermeta">
    <!-- Customize the title -->
    <template #title>
      Search Users
    </template>

    <!-- Customize the search form -->
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

    <!-- Customize the table header -->
    <template #table-header>
      <th>User</th>
      <th>Credentials</th>
      <th>Questions</th>
      <th>Session Info</th>
      <th>Created At</th>
      <th>Last Updated</th>
    </template>

    <!-- Customize the table body -->
    <template #table-body="{ results }">
      <tr v-for="(meta, index) in results" :key="index">
        <td>
          <router-link :to="{ name: 'UserMetaDetail', params: { username: meta.user_username } }">
            {{ meta.user_username }}
          </router-link>
        </td>
        <td>{{ meta.credentials }}</td>
        <td>{{ meta.questions }}</td>
        <td>{{ meta.session_info }}</td>
        <td>{{ meta.created_at }}</td>
        <td>{{ meta.updated_at }}</td>
      </tr>
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
};
</script>
