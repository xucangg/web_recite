<template>
    <div class="content">
        <div class="nologin">
            <h1>欢迎使用</h1>
            <div>
                <h3>词库已有 <span style="color:#1bff00b5">{{wordslength.total}}</span> 单词</h3>
                    <el-row>
                        <el-col :span='12' class="type">cte4: <span style="color:#f56c6c">{{wordslength.countcte4}}</span></el-col>
                        <el-col :span='12' class="type">cte6: <span style="color:#f56c6c">{{wordslength.countcte6}}</span></el-col>
                    </el-row>    
            </div>
            <h2><a href="/#/model">点击开始</a></h2>
        </div>
        <div class="logined" hidden="true">
            <h1>欢迎回来</h1>
            <div>
                <h3>您已学习单词：</h3>
                <li>
                    <ol></ol>
                </li>
            </div>
        </div>
    </div>
</template>

<script>
import {words} from '../axios/axios.js'


export default {
    data(){
        return{
            wordslength:{},
        };
    },

    created(){
        this.getWordCount();
    },

    methods:{
        getWordCount(){
            words().then((Response)=>{
                this.wordslength = Response.data[0];
            });
        },
    }
}
</script>

<style>
    .content{
    text-align:center;
    }
    body{
        background-color: #fff;
    }
    .bg{
        min-height: 100vh;
    }
    .content{
        padding-top: 70px;
    }
    h1{
        padding-top: 120px;
    }
    h2{
        padding-top: 40px;
    }
    h3{
        padding-top: 20px;
        padding-bottom: 20px
    }
    .type{
        display: inline-block;
    }

</style>