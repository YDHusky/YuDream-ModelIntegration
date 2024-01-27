<script setup lang="ts">

import MainHeaderNav from "@/components/main/MainHeaderNav.vue";
let is_login = defineModel()

</script>

<template>
   <div class="common-layout">
    <el-container>
      <el-header>
        <MainHeaderNav v-model="is_login"></MainHeaderNav>
      </el-header>
      <el-main>
        <router-view v-model="is_login"/>
      </el-main>
    </el-container>
  </div>
</template>

<style>
.common-layout {
  height: 100%;
  width: 100%;
  .el-header {
    padding: 0;
  }
}
</style>