-- Who tried to blind the trail this week?
SELECT eventtime,
       useridentity.arn,
       sourceipaddress,
       eventname,
       errorcode
FROM cloudtrail_logs
WHERE "timestamp" >= '2026/09/20'  -- partition column: scan one week
  AND eventsource = 'cloudtrail.amazonaws.com'
  AND eventname IN ('StopLogging', 'DeleteTrail',
                    'UpdateTrail', 'PutEventSelectors')
ORDER BY eventtime;
