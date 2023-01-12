<template>
<div id="my_works" class="flex flex-row h-96 bg-green-500">
    <div class="h-full" :class="w-1/`${works.length}`" v-for="work in works">
        <WorkItem :title="`${work.title}`" :description="`${work.description}`"/>
    </div>
</div>
</template>

<script>
import WorkItem from './WorkItem.vue';
export default {
    name: "Works",
    data() {
        return {
            works: [ 
                { image: "tree_leaves.jpg", title: "title1", description: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum." },
                { image: "tree_leaves.jpg", title: "title2", description: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum." },
                { image: "tree_leaves.jpg", title: "title3", description: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum." },
            ],
        }
    },
    mounted() {
        let size = 255;
        for (let i = 0; i < this.works.length; i++) {
            if (this.works[i].description.length > size) {
                this.works[i].description = this.works[i].description.slice(0, size) + '...';
            }
        }
    },
    methods: {
        
    },
    components: { WorkItem }
}
</script>