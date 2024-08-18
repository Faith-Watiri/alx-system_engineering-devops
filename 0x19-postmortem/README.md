Issue Summary:

Duration: The outage lasted for 2 hours, from 12:00 PM to 2:00 PM UTC on August 16, 2024.
Impact: The company's primary web application experienced a severe slowdown, rendering pages at an average of 20 seconds per load. Approximately 75% of users were affected, leading to significant frustration and abandoned sessions. E-commerce transactions dropped by 40% during the outage.
Root Cause: The root cause was a misconfigured database index that led to a full table scan during peak traffic, overwhelming the database and causing the application to slow down significantly.
Timeline:

12:05 PM - Issue detected via a spike in response time alerts from the monitoring system.
12:10 PM - The on-call engineer noticed increased latency on key API endpoints.
12:15 PM - Initial investigation began by checking the application servers for resource constraints.
12:25 PM - No issues found on the application servers; focus shifted to the database.
12:30 PM - A misleading path: Network latency was suspected due to recent changes in the firewall configuration, but no issues were found.
12:45 PM - The incident was escalated to the database team for deeper analysis.
1:00 PM - Database team identified a significant increase in query execution time for specific endpoints.
1:15 PM - The root cause was identified as a missing index on a frequently queried table.
1:30 PM - A temporary fix was implemented by manually adding the required index.
2:00 PM - Full service was restored, with response times returning to normal.
Root Cause and Resolution:

Root Cause: The issue was caused by a missing database index on a table that was heavily queried during peak hours. The application was recently updated to include more complex queries, which were not optimized due to the absence of an appropriate index. This led to full table scans, significantly increasing query execution time and causing the entire application to slow down.

Resolution: Once the issue was identified, the database team created the necessary index on the affected table. This immediately improved the performance of the problematic queries, reducing their execution time from over 15 seconds to under 200 milliseconds. The application returned to normal operation as soon as the index was applied.

Corrective and Preventative Measures:

Improvements:
Conduct a thorough review of database query performance after each application update.
Enhance monitoring to include alerts for slow query execution times, not just overall response times.
Improve communication between the application and database teams during deployment to ensure all necessary optimizations are in place.
Tasks:
TODO 1: Implement automated monitoring of slow queries using tools like pg_stat_statements and set up alerts.
TODO 2: Add a step in the deployment process to review query plans for any new or modified queries.
TODO 3: Patch the firewall configuration to log any potential network latency issues more effectively.
TODO 4: Schedule a training session for the development team on database indexing best practices.
TODO 5: Review all recent changes in the database schema and apply necessary indexes to prevent similar issues.
This postmortem aims to prevent future occurrences of such an outage by improving our monitoring, deployment processes, and team communication.








HUMOUR ADDED POSTMORTEM
Postmortem Report: The Great Snail Race of August 2024 🐌
Issue Summary:

Duration: The web app experienced "snail mode" for 2 hours, from 12:00 PM to 2:00 PM UTC on August 16, 2024.
Impact: Imagine trying to load a webpage and having time to make a coffee, finish a chapter of your book, and rethink your life choices—yeah, it was that slow. About 75% of our users were caught in this time warp, with page load times averaging 20 seconds. E-commerce sales took a nosedive, dropping by 40%.
Root Cause: A sneaky missing database index turned our usual lightning-fast queries into something more akin to a leisurely stroll through a swamp, resulting in a full table scan that bogged down the database.

Timeline:

12:05 PM - Alert! Our monitoring system cried wolf—response times were spiking faster than a toddler on a sugar high.
12:10 PM - The on-call engineer, halfway through a sandwich, saw the alert and did a classic spit-take.
12:15 PM - Initial investigation: "Is it the servers? Nah, they're chillin'."
12:25 PM - Focus shifted to the database. Maybe it was having a rough day?
12:30 PM - Red herring alert: Network latency was suspected. (Spoiler: it wasn’t the network.)
12:45 PM - Escalation: The database team was called in like the Avengers.
1:00 PM - "Houston, we have a problem"—queries were dragging their feet.
1:15 PM - Bingo! A missing index was the culprit, hiding in plain sight.
1:30 PM - The database team added the index faster than you can say "optimization."
2:00 PM - And we're back! The app zoomed back to life, much to the relief of our caffeine-deprived users.
Root Cause and Resolution:

Root Cause: The trouble started when we rolled out some snazzy new features. Unfortunately, we forgot to invite a crucial guest to the party—an index on a frequently queried table. This oversight led to our database running around in circles (figuratively speaking), performing full table scans that slowed everything down to a crawl.

Resolution: Our database team swooped in and added the missing index, which was like giving the database a turbo boost. Query times dropped from a sluggish 15 seconds to a brisk 200 milliseconds, and the app was back to its usual peppy self.

Corrective and Preventative Measures:

Improvements:

Next time we change the app, we'll make sure the database gets the memo. We're adding a step to review query performance post-deployment.
We're also beefing up our monitoring so we can catch these slow queries before they spiral out of control.
Communication is key—so we're setting up more frequent cross-team check-ins.
Tasks:

TODO 1: Set up automated alerts for slow queries using tools like pg_stat_statements. We don't want any more surprise marathons.
TODO 2: Introduce a query plan review in our deployment checklist. No more missing indexes on our watch!
TODO 3: Log network latency more effectively, just in case the network decides to play tricks on us in the future.
TODO 4: Organize a "Database Indexing 101" session for the development team. We'll make it fun, promise!
TODO 5: Go through recent database changes and ensure every table has the right indexing in place.
And that, folks, is how we turned a slow day into a learning opportunity. Lessons were learned, laughs were had, and our web app is faster than ever!
