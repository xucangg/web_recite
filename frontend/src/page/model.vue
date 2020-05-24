<template>
    <div class='model'>
        <head-top></head-top>
        <div class='choose'>
            <form>
                <div class="choose_level">
                <h3>选择词汇级别：</h3>
                <ul>
                    <li>
                        <input type="radio" name="level" v-model="level" value="cte-4">
                        <span>Cte-4</span>
                    <li>
                    <li>
                        <input type="radio" name="level" v-model="level" value="cte-6">
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
                    <input type="text" name='amount' v-model="num" placeholder="最大不超过20个">
                </div>
                <input type="button" @click="model" value="随机生成单词">
                <input type="button" @click="model" value="按首字母生成单词">
            </form>
        </div>
    </div>
</template>


<script>
import headTop from '../components/headTop'

export default {
    inject: ['reload'],
    data(){
        return {
            level: "",
            translate: "",
            num: "",
            returnWords:""
        }
    },
    
    methods:{
        model(){
            if (this.num > 20){
                alert('最多生成20个单词')
                this.num = null
                return
            }
            this.$router.push({name:'recite', params:{
                level:this.level,
                translate:this.translate,
                num:this.num,
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

</style>