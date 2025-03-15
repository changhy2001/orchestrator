<template>
  <div class="container mt-4">
    <h2>Select a Data Table</h2>
    <!-- Add the grid gap class to the row -->
    <div class="row g-4">
      <!-- Loop through the list of data tables and create a card for each -->
      <div class="col-md-4" v-for="(table, index) in dataTables" :key="index">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">{{ table.title }}</h5>
            <p class="card-text">{{ table.description }}</p>
            <!-- Clicking this link navigates to the route for that data table -->
            <router-link :to="table.route" class="btn btn-primary">
              Open
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AppHomePage",
  data() {
    return {
      // Each item contains the info for one data table
      dataTables: [
        {
          title: "UserMeta",
          description: "Manage user data and credentials.",
          route: "/searchapp/usermeta",
        },
        {
          title: "UserMeta2",
          description: "Manage user data and credentials.",
          route: "/searchapp/usermeta",
        },
        {
          title: "UserMet3",
          description: "Manage user data and credentials.",
          route: "/searchapp/usermeta",
        },
      ],
    };
  },
};
</script>

<style scoped>
/* Simple spacing/styling. Adjust as needed. */
.container {
  max-width: 1200px;
  margin: 0 auto;
}
.card-title {
  font-weight: 600;
}

.row {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem; /* Adjust this value as needed */
}
</style>
