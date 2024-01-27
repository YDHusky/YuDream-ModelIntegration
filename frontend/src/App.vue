<script setup lang="ts">
import { RouterView } from 'vue-router'
import {ref, watch} from "vue";
import {user_info_md} from "@/services/modules/user";
let is_login = ref(sessionStorage.getItem("token")!==null);
let nickname = ref("")
let avatar = ref("")
let is_admin = ref(false)
const loadInfo = ()=>{
  let userData = user_info_md()
  userData.then((res)=>{
    nickname.value = res?.['nickname']
    avatar.value = res?.['avatar']
    if (res?.['role'] >=3 ) {
      is_admin.value = true
    }
  })
}
watch(is_login, (newVal, oldVal) => {
  if (newVal===true) {
    loadInfo()
  }
})
</script>

<template>

  <div class="main">
    <router-view v-model="is_login"/>
  </div>
</template>

<style scoped>
.main {
  height: 100vh;
  width: 100vw;
  background-color: #f5f5f5;
  align-items: center;
  text-align: center;
}
</style>
