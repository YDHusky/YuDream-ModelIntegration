<script setup lang="ts">
import {onMounted, ref} from "vue";
import {statistics_md} from "@/services/modules/user";
let statistics = ref({
  model_num: 0,
  works_num: 0
})
async function satisfies_async(){
  let res = await statistics_md()
  if (res.code === 200) {
    statistics.value['model_num'] = res.data['model']
    statistics.value['works_num'] = res.data['work']
  }
}
onMounted(() => {
  satisfies_async()
})
</script>

<template>
  <el-card header="统计">
    <el-row :gutter="50">
      <el-col :span="12">
        <el-statistic title="模型个数" :value="statistics['model_num']"></el-statistic>
      </el-col>
      <el-col :span="12">
        <el-statistic title="作品个数" :value="statistics['works_num']"></el-statistic>
      </el-col>
    </el-row>
  </el-card>
</template>

<style scoped>

</style>