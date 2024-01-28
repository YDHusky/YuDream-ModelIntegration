<script setup lang="ts">
import {ref} from "vue";
import {login_md} from "@/services/modules/user";
import router from "@/router";
import login_user from "@/entities/index";

let is_login = defineModel()
const form = ref<login_user>({
  username: "",
  password: "",
  checked: false
});
const submitForm = () => {
  asy_login(form.value)
};

async function asy_login(user: login_user) {
  try {
    let data = await login_md(user)
    if (data.code == 200) {
      sessionStorage.setItem("token", data.data['token'])
      router.push("/")
      is_login.value = true
    } else {
      console.log(data);
    }
  } catch (error) {
    console.log(error);
  }
}

</script>

<template>
  <div class="login-card">
    <el-card class="box-card" header="登录">
      <el-form :model="form" label-width="80px" label-position="top">
        <el-form-item label="用户名或电子邮件" prop="username">
          <el-input v-model="form.username"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input type="password" v-model="form.password"></el-input>
        </el-form-item>
        <el-form-item>
          <el-checkbox v-model="form.checked">记住我</el-checkbox>
        </el-form-item>
        <el-form-item>
          <el-button style="width: 100%" type="primary" @click="submitForm" @keydown.enter="submitForm">登录</el-button>
        </el-form-item>
        <el-form-item>
          <el-button link>忘记密码</el-button>
          <el-button @click="router.push('/register')" style="margin: 0 0 0 auto" link>还没有账号?点我注册</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<style scoped>
.el-form-item__label {
  display: flex;
  align-items: flex-start;
}
</style>