<script setup lang="ts">
import {onMounted, ref} from "vue";
import {getOption_md, updateOption_md} from "@/services/modules/option";
import {ElNotification} from "element-plus";

let announcement = ref('')
let announcement_drawer = ref(false)
async function get_announcement(){
  let res = await getOption_md('announcement')
  announcement.value = res['data']['value']
}
onMounted(() => {
  get_announcement()
})
const handleSelect = () => {
  announcement_drawer.value = true
}
async function update_announcement(){
  let res = await updateOption_md('announcement', announcement.value)
  if (res['code'] === 200) {
    announcement_drawer.value = false
    ElNotification({
      title: '成功',
      message: '公告更新成功',
      type: 'success'
    })
  }
  else {
    ElNotification({
      title: '失败',
      message: '公告更新失败',
      type: 'error'
    })
  }
}
</script>

<template>
  <div class="admin-setting">
    <el-card header="公告设置">
      <div>{{ announcement }}</div>
      <el-button @click="handleSelect">编辑公告</el-button>
    </el-card>
  </div>
  <el-drawer
    title="编辑公告"
    direction="rtl"
    v-model="announcement_drawer">
    <el-input
      type="textarea"
      :rows="5"
      placeholder="请输入内容"
      v-model="announcement">
    </el-input>
    <template #footer>
      <el-button @click="announcement_drawer = false">取 消</el-button>
      <el-button type="primary" @click="update_announcement">确 定</el-button>
    </template>
  </el-drawer>

</template>

<style scoped>
.admin-setting {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-between;
  margin: 0 auto;
  width: 100%;
  height: 100%;
  .el-button{
    margin-top: 20px;
    width: 100%;
  }
}
</style>