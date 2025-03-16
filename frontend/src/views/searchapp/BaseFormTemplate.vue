<template>
    <div class="base-form">
        <h2><slot name="title">Form</slot></h2>
        <form @submit.prevent="submitForm">
        <!-- Slot for form fields. We pass the current form data and an updater function -->
        <slot name="form-fields" :form="form" :updateForm="updateForm"></slot>
        <button type="submit" class="btn btn-primary">Submit</button>
        </form>
        <p v-if="error" class="error">{{ error }}</p>
    </div>
</template>

<script>
import axios from "axios";
import { getCookie } from '@/utils/cookie';

export default {
name: "BaseFormTemplate",
props: {
    initialForm: {
    type: Object,
    default: () => ({}),
    },
    apiEndpoint: {
    type: String,
    required: true,
    },
},
data() {
    return {
    form: { ...this.initialForm },
    error: null,
    };
},
methods: {
    // Generic method to update form fields
    updateForm(field, value) {
        this.$set(this.form, field, value);
    },
    // Generic submission method
    submitForm() {
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
            });
        },
    },
};
</script>

<style scoped>
.base-form {
    max-width: 600px;
    margin: auto;
    padding: 20px;
}
.error {
    color: red;
    margin-top: 10px;
}
</style>
