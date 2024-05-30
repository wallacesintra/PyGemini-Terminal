```kotlin  
        val query = FirebaseFirestore.getInstance().collection("cities")
                .whereEqualTo("state", "CO")
                .whereLessThan("population", 1000000L)  
```
