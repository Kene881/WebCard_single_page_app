<template>
    <div class="p-20 w-full h-full bg-green-500 opacity-75 hover:opacity-100 transition-opacity" >
        <h5 class="mb-2 text-6xl font-bold tracking-tight text-gray-900 dark:text-white">{{title}}</h5>
        <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">{{description}}</p>
    </div>
</template>

<script>
export default {
    name: "WorkItem",
    props: {
        image: String,
        title: String,
        description: String,
        count_works: Number
    }
}
</script>