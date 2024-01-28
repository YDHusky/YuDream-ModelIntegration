<script setup lang="ts">

import HeaderMenu from "@/components/user/HeaderMenu.vue";
import AdminAsideMenu from "@/components/admin/AdminAsideMenu.vue";
import {ref} from "vue";
const getHeight = () => {
  return window.innerHeight - 120 + 'px'
}
let height = ref(getHeight())
</script>

<template>
  <div class="common-layout">
    <el-container>
      <el-header class="header">
        <HeaderMenu/>
      </el-header>
      <el-container>
        <el-aside width="200px">
          <AdminAsideMenu></AdminAsideMenu>
        </el-aside>
        <el-main>
          <el-scrollbar :height="height">
            <router-view/>
          </el-scrollbar>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<style scoped>
.header {
  padding: 0;
}
</style>