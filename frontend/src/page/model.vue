<template>
    <div class='model'>
        <head-top></head-top>
        <div class='choose'>
            <form>
                <div class="choose_level">
                <h3>选择词汇级别：</h3>
                <ul>
                    <li>
                        <input type="radio" name="level" v-model="level" value="Cte4">
                        <span>Cte-4</span>
                    <li>
                    <li>
                        <input type="radio" name="level" v-model="level" value="Cte6">
                        <span>Cte-6</span>
                    </li>
                </ul>
                </div>
                <div>
                <h3>选择默写模式</h3>
                <ul>
                    <li>
                        <input type="radio" name="translate" v-model="translate" value="en">
                        <span>中转英</span>
                    </li>
                    <li>
                        <input type="radio" name="translate" v-model="translate" value="ch">
                        <span>英转中</span>
                    </li>
                </ul>
                </div>
                <div>
                    <h3>单词个数</h3>
                    <input class="num" type="text" name='amount' v-model="num" placeholder="最大不超过20个">
                </div>
                <button  @click="model" value="random">随机生成单词</button>
                <button  @click="model" value="initial">按首字母生成单词</button>
            </form>
        </div>
    </div>
</template>


<script>
import headTop from '../components/headTop'

export default {
    data(){
        return {
            level: "",
            translate: "",
            num: "",
        }
    },
    
    methods:{
        model(value){
            if (this.num > 20){
                alert('最多生成20个单词')
                this.num = null
                return
            }
            if(this.level === ''){
                this.$message("请选择单词等级")
                return
            }
            if(this.translate === ''){
                this.$message('请选择默写模式')
                return
            }
            if(this.num === ''){
                this.$message('请填写单词数量')
                return
            }
            this.$router.push({name:'recite', params:{
                level:this.level,
                translate:this.translate,
                num:this.num,
                model:value.target.value
                }});
        }
    },
 
    components:{
        headTop,
    }
    
}
</script>

<style>
.choose{
    padding-top: 70px;
    text-align: center;
}
.num{
    margin-bottom: 20px;
}

</style>