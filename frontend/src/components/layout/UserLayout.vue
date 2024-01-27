<script setup lang="ts">

import AsideMenu from "@/components/user/AsideMenu.vue";
import HeaderMenu from "@/components/user/HeaderMenu.vue";
import {ref} from "vue";

let is_expand = ref(false)
const getHeight = () => {
  return window.innerHeight - 120 + 'px'
}
let height = ref(getHeight())
</script>

<template>
  <div class="common-layout">
    <el-container>
      <el-header class="header">
        <HeaderMenu v-model="is_expand"></HeaderMenu>
      </el-header>
      <el-container>
        <el-aside width="200px">
          <AsideMenu v-model="is_expand"></AsideMenu>
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
.header{
  padding: 0;
}
</style>