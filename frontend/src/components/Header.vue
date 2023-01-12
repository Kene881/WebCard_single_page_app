<template>
    <div class="flex justify-around bg-green-500 h-8 text-white py-0.5">
        <span>web</span>
        <span>web</span>
        <span>web</span>
        <span>web</span>
        <span>web</span>
        <span>web</span>
        <span>web</span>
    </div>
    <!-- bg-[url('https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/bc502803-57e4-4628-9e9c-e7b36d03edce/djtlyu-a1026af9-fb3c-4a9f-8fdd-11545158c0ba.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2JjNTAyODAzLTU3ZTQtNDYyOC05ZTljLWU3YjM2ZDAzZWRjZVwvZGp0bHl1LWExMDI2YWY5LWZiM2MtNGE5Zi04ZmRkLTExNTQ1MTU4YzBiYS5qcGcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.FXYntG9XSqrfWr7C9MTHdJnmE9uQeY4JIG_TswUIWew')]  -->
    <div class="flex flex-col justify-center items-center py-16 px-4 mx-auto bg-[url('/src/assets/lines.jpg')] bg-cover">
        <h1 class="pb-5 text-6xl text-center text-white dark:text-gray-100 transition-colors">
        Web developer 
        </h1>
        <h4 class="pb-20 text-2xl text-center text-white dark:text-gray-100 transition-colors">
        Vuejs Tailwind FastApi
        </h4>

        <div class="flex justify-center pb-10 space-x-4">
        <a
            rel="noopener"
            href="#contact_with_me"
            class="inline-flex items-center py-4 px-6 space-x-1 font-medium text-indigo-50 bg-green-700 hover:bg-green-900 rounded-md shadow-xl hover:shadow-md transition duration-300"
        >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"></path></svg>
            <span>Сontact with me</span>
        </a>

        <a
            rel="noopener"
            href="#my_works"
            class="inline-flex items-center py-4 px-6 space-x-1 font-medium text-indigo-50 bg-green-700 hover:bg-green-900 rounded-md shadow-xl hover:shadow-md transition duration-300"
        >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"></path></svg>
            <span>Work examples</span>
        </a>
        </div>
    </div>
</template>

<script>
export default {
    name: "Header",
}
</script>