<script setup lang="ts">
import {onMounted, ref} from "vue";
import {update_user_info_md, update_user_password_md, user_info_md} from "@/services/modules/user";
import {baseURL} from "@/services/requests/config";
import {ElNotification} from "element-plus";

let avatar = ref("")

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
let nickName = ref("")
let email = ref("")
let phone = ref("")
const loadInfo = () => {
  let userData = user_info_md()
  userData.then((res) => {
    nickName.value = res?.['nickname']
    email.value = res?.['email']
    phone.value = res?.['phone']
    avatar.value = res?.['avatar']
  })
}
async function update_user_info_async(){
  if (nickName.value == "" || email.value == "" || phone.value == "" || nickName.value == null || email.value == null || phone.value == null){
    ElNotification({
      title: "信息不能为空",
      type: "error"
    })
    return
  }
  else {
    let data = await update_user_info_md({
      nickname: nickName.value,
      email: email.value,
      phone: phone.value
    })
    if (data.code == 200){
      ElNotification({
        title: "修改成功",
        type: "success"
      })
    }
    else {
      ElNotification({
        title: "修改失败",
        type: "error"
      })
    }
  }
}
let password = ref({
  old: "",
  new: "",
  confirm: ""
})
async function update_user_password_async(){
  if (password.value.new != password.value.confirm){
    ElNotification({
      title: "两次密码不一致",
      type: "error"
    })
    return
  }
  else {
    let data = await update_user_password_md({
      old_password: password.value.old,
      new_password: password.value.new
    })
    if (data.code == 200){
      ElNotification({
        title: "修改成功",
        type: "success"
      })
    }
    else {
      ElNotification({
        title: "修改失败",
        type: "error"
      })
    }
  }
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
    <div class="password">
      <el-card header="更改密码">
        <el-form label-position="top">
          <el-form-item label="原密码">
            <el-input v-model="password.old" type="password" placeholder="请输入原密码"></el-input>
          </el-form-item>
          <el-form-item label="新密码">
            <el-input v-model="password.new" type="password" placeholder="请输入新密码"></el-input>
          </el-form-item>
          <el-form-item label="确认密码">
            <el-input v-model="password.confirm" type="password" placeholder="请再次输入新密码"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button @click="update_user_password_async" type="primary">确认修改</el-button>
          </el-form-item>
        </el-form>
      </el-card>
    </div>
    <div class="base-info">
      <el-card header="基本信息">
        <el-form label-position="top">
          <el-form-item label="昵称">
            <el-input v-model="nickName" placeholder="请输入昵称"></el-input>
          </el-form-item>
          <el-form-item label="邮箱">
            <el-input v-model="email" placeholder="请输入邮箱"></el-input>
          </el-form-item>
          <el-form-item label="手机号">
            <el-input v-model="phone" placeholder="请输入手机号"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="update_user_info_async">确认修改</el-button>
          </el-form-item>
        </el-form>
      </el-card>

    </div>
  </div>
</template>

<style>
.setting-page {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;

  .el-button {
    margin-top: 10px;
    width: 100%;
  }

  .avatar {
    width: 30%;
    height: 100%;
    margin: 0 10px 0 0;
  }

  .password {
    width: 30%;
    height: 100%;
    margin: 0 10px 0 0;
  }

  .base-info {
    width: 30%;
    height: 100%;
    margin: 0 0 0 10px;
  }
}
</style>