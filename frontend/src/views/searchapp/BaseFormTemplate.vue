<template>
    <div class="base-form-template">
      <h2><slot name="title">Form</slot></h2>
      <form @submit.prevent="handleSubmit">
        <!-- The slot passes the form object so that the parent can bind fields -->
        <slot name="form" :form="form"></slot>
        <div class="form-actions">
          <button type="submit" class="btn btn-success">Submit</button>
          <button type="button" class="btn btn-secondary" @click="handleCancel">Cancel</button>
        </div>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: "BaseFormTemplate",
    props: {
      // Pass an initial form object if needed
      initialForm: {
        type: Object,
        default: () => ({}),
      },
    },
    data() {
      return {
        form: { ...this.initialForm },
      };
    },
    methods: {
      handleSubmit() {
        // Emit the current form data on submission
        this.$emit("submit", this.form);
      },
      handleCancel() {
        // Emit cancel event so parent can decide what to do (e.g., navigate away)
        this.$emit("cancel");
      },
    },
  };
  </script>
  
  <style scoped>
  .base-form-template {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
  }
  .form-actions {
    margin-top: 15px;
    display: flex;
    gap: 10px;
  }
  </style>
  