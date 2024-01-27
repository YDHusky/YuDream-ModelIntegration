<script setup lang="ts">
import {onMounted, ref} from "vue";
import {user_info_md} from "@/services/modules/user";
import {baseURL} from "@/services/requests/config";
import {ElNotification} from "element-plus";
let avatar = ref("")
const loadInfo = () => {
  let userData = user_info_md()
  userData.then((res) => {
    avatar.value = res?.['avatar']
  })
}
onMounted(() => {
  loadInfo()
})
let avatarDrawer = ref(false)
let uploadInfo = ref({
  action: baseURL + "/info/update/avtar",
  headers: {
    Authorization: "Bearer " + sessionStorage.getItem("token")
  }
})
const uploadError = () => {
  ElNotification({
    title: "上传失败",
    type: "error"
  })
}
</script>

<template>
  <div class="setting-page">
    <div class="avatar">
      <el-card header="更改头像">
        <el-avatar :size="50" :src="avatar"/>
        <el-upload
            method="post"
            name="avtar"
          :action="uploadInfo.action"
          :headers="uploadInfo.headers"
          :show-file-list="false"
          :on-success="loadInfo"
            :on-error="uploadError"
        >
          <el-button>点击更换</el-button>
        </el-upload>
      </el-card>
    </div>
  </div>
</template>

<style>
.setting-page {
  width: 100%;
  height: 100%;
  display: flex;

  .el-button {
    margin-top: 10px;
    width: 100%;
  }
}
</style>