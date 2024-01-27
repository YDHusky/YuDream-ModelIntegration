<script setup lang="ts">
import {ref} from "vue";

let announcement = ref("暂无，系统正在开发中！")
</script>

<template>
  <el-row :gutter="40">
    <el-col :span="15">
      <el-card header="使用统计">
        <el-row>
          <el-col :span="8">
            <el-statistic title="模型个数" :value="1"/>
          </el-col>
          <el-col :span="8">
            <el-statistic title="作品个数" :value="5"/>
          </el-col>
          <el-col :span="8">
            <el-statistic title="收藏个数" :value="2"/>
          </el-col>
        </el-row>
      </el-card>
    </el-col>
    <el-col :span="8">
      <el-card header="公告">
        {{ announcement }}
      </el-card>
    </el-col>
  </el-row>
</template>

<style scoped>

</style>