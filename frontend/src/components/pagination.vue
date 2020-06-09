<template>
    <div>
        <div class="index_tableFoot">
            <div class="index_pagination">
                <ul class="index_pageContainer">
                    <li v-for="page in pages" :key="page.id" @click='pageCallback(page.page)' :class="[page.active?'index_active':'',page.banclick?'ban':'',page.index_nomore?'index_nomore':'']">{{page.text}}</li>
                </ul>
             </div>
        </div>
    </div>
</template>



<script>
export default {
    props:{
        preText:{
            type:String,
            default:'上一页'
            },
        nextText:{
            type:String,
            default:'下一页'
            },
        page:[String,Number],
        totalPage:[String, Number]
    },
    
    methods:{
        pagina(curpage,endpage){
            var pages = []
            if(curpage<=1 && endpage===1) {pages.push({text:endpage,active:true});return pages}
            var d = 1
            curpage-1===0?pages.push({text:this.preText,index_nomore:true}):pages.push({page:curpage-1,text:this.preText})
            if(curpage>4) d = curpage-2,pages.push({page:1,text:1}),pages.push({text:'...',banclick:true})
            if(endpage-curpage>=0 && curpage>=1) for(; d<curpage;d++) pages.push({page:d,text:d})
            pages.push({page:curpage,text:curpage,active:true})
            var e = 1
            if(endpage-curpage<=3){e = curpage+1;for(;e<=endpage;e++) pages.push({page:e,text:e})}
            if(endpage-curpage>3){
                e = curpage+1;
                for(;e<=curpage+2;e++){pages.push({page:e,text:e})}
                pages.push({text:'...',banclick:true})
                pages.push({page:endpage,text:endpage})
                }
            curpage-endpage===0?pages.push({text:this.nextText,index_nomore:true}):pages.push({page:curpage+1,text:this.nextText})
            return pages
        },
        pageCallback:function(page){
            this.$emit('pagefn',{page:page})
      }
    },

    computed:{
        pages:function(){
            return this.pagina(parseInt(this.page),this.totalPage)
        }
    }
}
</script>


<style>
.index_tableFoot{
    margin-top: 50px;
    padding: 0 10%;
}
.index_pageContainer > li{
    list-style: none;
    float: left;
    padding: 0 8px;
    cursor: pointer;
    border: 1px solid #ccc;
    height: 28px;
    line-height: 28px;
    margin-right: 8px;
}
.index_nomore{
    color: #b5b5b5!important;
    cursor: not-allowed!important;
}
.index_active{
    color: #fff!important;
    background: #28bea0;
    border-radius: 1px;
}
.ban{
    pointer-events:none;
}
</style>