<script setup lang="ts">

import UserOptionCard from "@/views/admin/cpn/UserOptionCard.vue";
import UserCard from "@/views/admin/cpn/UserCard.vue";
import { onMounted, ref, watch} from "vue";
import {get_all_users_md, get_user_by_username_md, user_info_md} from "@/services/modules/user";

let user_list = ref()
let user = ref('')

async function get_user_list() {
  let res = await get_all_users_md()
  user_list.value = res['data']
}

async function get_user_info() {

  let res = await get_user_by_username_md(user.value)
  user_list.value = res['data']
}

onMounted(() => {
  get_user_list()
})
watch(user, () => {
  if (user.value !== '') {
    get_user_info()
  }
  else {
    get_user_list()
  }
})
</script>

<template>
  <div class="user-admin-page">
    <UserOptionCard v-model="user"></UserOptionCard>
    <div class="user-list">
      <UserCard v-model="user_list"></UserCard>
    </div>
  </div>
</template>

<style scoped>
.user-list {
  margin-top: 20px;
}
</style>