<script setup lang="ts">
import {onMounted, ref} from "vue";
import {get_statistics_admin_md} from "@/services/modules/user";
import {getOption_md} from "@/services/modules/option";
import router from "@/router";
let announcement = ref('')
let statistics = ref({
  model_num: 0,
  works_num: 0,
  user_num: 0
})
async function get_announcement(){
  let res = await getOption_md('announcement')
  announcement.value = res['data']['value']
}
async function satisfies_async(){
  let res = await get_statistics_admin_md()
  if (res.code === 200) {
    statistics.value['model_num'] = res.data['model']
    statistics.value['works_num'] = res.data['work']
    statistics.value['user_num'] = res.data['user']
  }
}
onMounted(() => {
  satisfies_async()
  get_announcement()
})
</script>

<template>
  <el-card header="数据统计">
    <el-row :gutter="50">
      <el-col :span="8">
        <el-statistic title="模型个数" :value="statistics['model_num']"></el-statistic>
      </el-col>
      <el-col :span="8">
        <el-statistic title="作品个数" :value="statistics['works_num']"></el-statistic>
      </el-col>
      <el-col :span="8">
        <el-statistic title="用户个数" :value="statistics['user_num']"></el-statistic>
      </el-col>
    </el-row>
  </el-card>
  <div class="announcement">
    <el-card header="公告">
      <div>{{ announcement }}</div>
      <el-button @click="router.push('/admin/setting')">前往编辑</el-button>
    </el-card>
  </div>
</template>

<style>
.announcement{
  margin-top: 20px;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  .el-button{
    margin-top: 20px;
    width: 100%;
  }
}
</style>