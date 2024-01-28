<script setup lang="ts">
import {ref} from "vue";
import {register_md} from "@/services/modules/user";
import {ElNotification} from "element-plus";
import router from "@/router";

let formData = ref({
  username: "",
  password: "",
  nickname: "",
  confirm: "",
  phone: ""
})
async function register_async(){
  if (formData.value.username == "" || formData.value.password == "" || formData.value.nickname == "" || formData.value.confirm == "" || formData.value.phone == ""){
    ElNotification({
      title: "信息不能为空",
      message: "请填写完整信息",
      type: "error"
    })
    return
  }
  else if (formData.value.password != formData.value.confirm){
    ElNotification({
      title: "两次密码不一致",
      message: "请重新输入密码",
      type: "error"
    })
    return
  }
  else {
    let data = await register_md({
      username: formData.value.username,
      password: formData.value.password,
      nickname: formData.value.nickname,
      phone: formData.value.phone
    })
    if (data.code == 200){
      ElNotification({
        title: "注册成功",
        message: "即将前往登录页面",
        type: "success"
      })
      router.push("/login")
    }
    else {
      ElNotification({
        title: "注册失败",
        message: data.message,
        type: "error"
      })
    }
  }
}
</script>

<template>
  <div class="register-card">
    <el-card header="注册">
      <el-form label-position="top">
        <el-form-item label="用户名">
          <el-input v-model="formData.username"></el-input>
        </el-form-item>
        <el-form-item label="昵称">
          <el-input v-model="formData.nickname"></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input type="password" v-model="formData.password"></el-input>
        </el-form-item>
        <el-form-item label="确认密码">
          <el-input type="password" v-model="formData.confirm"></el-input>
        </el-form-item>
        <el-form-item label="手机号">
          <el-input v-model="formData.phone"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button @click="register_async"  type="primary">注册</el-button>
        </el-form-item>
      </el-form>

    </el-card>
  </div>
</template>

<style>
.register-card{
  .el-button{
    margin-top: 10px;
    width: 100%;
  }
}
</style>