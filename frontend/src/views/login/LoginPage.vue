<script setup lang="ts">

import LoginCard from "@/views/login/cpn/LoginCard.vue";
let is_login = defineModel()
</script>

<template>
  <LoginCard class="card" v-model="is_login" ></LoginCard>
</template>

<style scoped>
.card{
  width: 400px;
  margin: 0 auto;
}
</style>