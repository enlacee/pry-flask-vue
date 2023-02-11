<template>
  <div class="relative bg-gray-100 sm:items-center sm:pt-0">

    <h2 class="text-2xl leading-7 font-semibold">
      {{ message }}
    </h2>

    <p class="mt-4 pt-4 text-gray-800 border-t border-dashed">
      To get started, remove
      <code class="bg-gray-100 text-sm p-1 rounded border"
        >components/TheIntro.vue</code
      >
    </p>
  </div>
</template>
<script>
export default {
  data () {
    return {
      message: 'New message from VueJS'
    }
  },
  created() {
    this.getMessage();
  },
  methods: {
    async getMessage() {
      const url = 'http://localhost:5000/api/v1.0/message';
      const rs = await fetch(url)
        .then(response => {
          if (!response.ok) {
            throw new Error(response.statusText);
          }
          return response.json();
        });

      this.message = rs.message;
    }
  }
}
</script>
