<script setup lang="ts">
let imageUrl = defineModel()
</script>

<template>
  <el-card class="output" header="输出预览">
    <el-scrollbar height="30%">
      <el-image class="image" fit="contain" :src="imageUrl"></el-image>
      <el-button class="out-button" type="primary">下载</el-button>
    </el-scrollbar>
  </el-card>

</template>

<style scoped>
.out-button {
  width: 100%;
  margin: 10px auto 5px auto;
}

.image {
  max-width: 100%;
  max-height: 400px;
}
</style>