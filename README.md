# DS_lab_9
```
rs.status()
{
        "set" : "rs0",
        "date" : ISODate("2019-11-02T01:11:26.837Z"),
        "myState" : 2,
        "term" : NumberLong(1),
        "syncingTo" : "node3:27017",
        "syncSourceHost" : "node3:27017",
        "syncSourceId" : 2,
        "heartbeatIntervalMillis" : NumberLong(2000),
        "majorityVoteCount" : 2,
        "writeMajorityCount" : 2,
        "optimes" : {
                "lastCommittedOpTime" : {
                        "ts" : Timestamp(1572657078, 1),
                        "t" : NumberLong(1)
                },
                "lastCommittedWallTime" : ISODate("2019-11-02T01:11:18.891Z"),
                "readConcernMajorityOpTime" : {
                        "ts" : Timestamp(1572657078, 1),
                        "t" : NumberLong(1)
                },
                "readConcernMajorityWallTime" : ISODate("2019-11-02T01:11:18.891Z"),
                "appliedOpTime" : {
                        "ts" : Timestamp(1572657078, 1),
                        "t" : NumberLong(1)
                },
                "durableOpTime" : {
                        "ts" : Timestamp(1572657078, 1),
                        "t" : NumberLong(1)
                },
                "lastAppliedWallTime" : ISODate("2019-11-02T01:11:18.891Z"),
                "lastDurableWallTime" : ISODate("2019-11-02T01:11:18.891Z")
        },
        "lastStableRecoveryTimestamp" : Timestamp(1572657049, 1),
        "lastStableCheckpointTimestamp" : Timestamp(1572657049, 1),
        "members" : [
                {
                        "_id" : 0,
                        "name" : "node1:27017",
                        "ip" : "172.31.45.188",
                        "health" : 1,
                        "state" : 2,
                        "stateStr" : "SECONDARY",
                        "uptime" : 1629,
                        "optime" : {
                                "ts" : Timestamp(1572657078, 1),
                                "t" : NumberLong(1)
                        },
                        "optimeDate" : ISODate("2019-11-02T01:11:18Z"),
                        "syncingTo" : "node3:27017",
                        "syncSourceHost" : "node3:27017",
                        "syncSourceId" : 2,
                        "infoMessage" : "",
                        "configVersion" : 1,
                        "self" : true,
                        "lastHeartbeatMessage" : ""
                },
                {
                        "_id" : 1,
                        "name" : "node2:27017",
                        "ip" : "172.31.46.39",
                        "health" : 1,
                        "state" : 2,
                        "stateStr" : "SECONDARY",
                        "uptime" : 1609,
                        "optime" : {
                                "ts" : Timestamp(1572657078, 1),
                                "t" : NumberLong(1)
                        },
                        "optimeDurable" : {
                                "ts" : Timestamp(1572657078, 1),
                                "t" : NumberLong(1)
                        },
                        "optimeDate" : ISODate("2019-11-02T01:11:18Z"),
                        "optimeDurableDate" : ISODate("2019-11-02T01:11:18Z"),
                        "lastHeartbeat" : ISODate("2019-11-02T01:11:26.386Z"),
                        "lastHeartbeatRecv" : ISODate("2019-11-02T01:11:26.203Z"),
                        "pingMs" : NumberLong(0),
                        "lastHeartbeatMessage" : "",
                        "syncingTo" : "node3:27017",
                        "syncSourceHost" : "node3:27017",
                        "syncSourceId" : 2,
                        "infoMessage" : "",
                        "configVersion" : 1
                },
                {
                        "_id" : 2,
                        "name" : "node3:27017",
                        "ip" : "172.31.45.70",
                        "health" : 1,
                        "state" : 1,
                        "stateStr" : "PRIMARY",
                        "uptime" : 1609,
                        "optime" : {
                                "ts" : Timestamp(1572657078, 1),
                                "t" : NumberLong(1)
                        },
                        "optimeDurable" : {
                                "ts" : Timestamp(1572657078, 1),
                                "t" : NumberLong(1)
                        },
                        "optimeDate" : ISODate("2019-11-02T01:11:18Z"),
                        "optimeDurableDate" : ISODate("2019-11-02T01:11:18Z"),
                        "lastHeartbeat" : ISODate("2019-11-02T01:11:26.385Z"),
                        "lastHeartbeatRecv" : ISODate("2019-11-02T01:11:26.385Z"),
                        "pingMs" : NumberLong(0),
                        "lastHeartbeatMessage" : "",
                        "syncingTo" : "",
                        "syncSourceHost" : "",
                        "syncSourceId" : -1,
                        "infoMessage" : "",
                        "electionTime" : Timestamp(1572655488, 1),
                        "electionDate" : ISODate("2019-11-02T00:44:48Z"),
                        "configVersion" : 1
                }
        ],
        "ok" : 1,
        "$clusterTime" : {
                "clusterTime" : Timestamp(1572657078, 1),
                "signature" : {
                        "hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
                        "keyId" : NumberLong(0)
                }
        },
        "operationTime" : Timestamp(1572657078, 1)
}



rs.config()
{
        "_id" : "rs0",
        "version" : 1,
        "protocolVersion" : NumberLong(1),
        "writeConcernMajorityJournalDefault" : true,
        "members" : [
                {
                        "_id" : 0,
                        "host" : "node1:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 1,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                },
                {
                        "_id" : 1,
                        "host" : "node2:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 1,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                },
                {
                        "_id" : 2,
                        "host" : "node3:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 1,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                }
        ],
        "settings" : {
                "chainingAllowed" : true,
                "heartbeatIntervalMillis" : 2000,
                "heartbeatTimeoutSecs" : 10,
                "electionTimeoutMillis" : 10000,
                "catchUpTimeoutMillis" : -1,
                "catchUpTakeoverDelayMillis" : 30000,
                "getLastErrorModes" : {

                },
                "getLastErrorDefaults" : {
                        "w" : 1,
                        "wtimeout" : 0
                },
                "replicaSetId" : ObjectId("5dbcd17418f8bd2e75844753")
        }
}
```


```
rs.status()
{
        "set" : "rs0",
        "date" : ISODate("2019-11-02T01:24:34.789Z"),
        "myState" : 1,
        "term" : NumberLong(2),
        "syncingTo" : "",
        "syncSourceHost" : "",
        "syncSourceId" : -1,
        "heartbeatIntervalMillis" : NumberLong(2000),
        "majorityVoteCount" : 2,
        "writeMajorityCount" : 2,
        "optimes" : {
                "lastCommittedOpTime" : {
                        "ts" : Timestamp(1572657858, 5),
                        "t" : NumberLong(2)
                },
                "lastCommittedWallTime" : ISODate("2019-11-02T01:24:18.586Z"),
                "readConcernMajorityOpTime" : {
                        "ts" : Timestamp(1572657858, 5),
                        "t" : NumberLong(2)
                },
                "readConcernMajorityWallTime" : ISODate("2019-11-02T01:24:18.586Z"),
                "appliedOpTime" : {
                        "ts" : Timestamp(1572657858, 5),
                        "t" : NumberLong(2)
                },
                "durableOpTime" : {
                        "ts" : Timestamp(1572657858, 5),
                        "t" : NumberLong(2)
                },
                "lastAppliedWallTime" : ISODate("2019-11-02T01:24:18.586Z"),
                "lastDurableWallTime" : ISODate("2019-11-02T01:24:18.586Z")
        },
        "lastStableRecoveryTimestamp" : Timestamp(1572657825, 1),
        "lastStableCheckpointTimestamp" : Timestamp(1572657825, 1),
        "electionCandidateMetrics" : {
                "lastElectionReason" : "stepUpRequestSkipDryRun",
                "lastElectionDate" : ISODate("2019-11-02T01:21:05.569Z"),
                "termAtElection" : NumberLong(2),
                "lastCommittedOpTimeAtElection" : {
                        "ts" : Timestamp(1572657658, 1),
                        "t" : NumberLong(1)
                },
                "lastSeenOpTimeAtElection" : {
                        "ts" : Timestamp(1572657658, 1),
                        "t" : NumberLong(1)
                },
                "numVotesNeeded" : 2,
                "priorityAtElection" : 1,
                "electionTimeoutMillis" : NumberLong(10000),
                "priorPrimaryMemberId" : 2,
                "numCatchUpOps" : NumberLong(892810288),
                "newTermStartDate" : ISODate("2019-11-02T01:21:05.924Z"),
                "wMajorityWriteAvailabilityDate" : ISODate("2019-11-02T01:21:07.214Z")
        },
        "members" : [
                {
                        "_id" : 0,
                        "name" : "node1:27017",
                        "ip" : "172.31.45.188",
                        "health" : 1,
                        "state" : 1,
                        "stateStr" : "PRIMARY",
                        "uptime" : 2417,
                        "optime" : {
                                "ts" : Timestamp(1572657858, 5),
                                "t" : NumberLong(2)
                        },
                        "optimeDate" : ISODate("2019-11-02T01:24:18Z"),
                        "syncingTo" : "",
                        "syncSourceHost" : "",
                        "syncSourceId" : -1,
                        "infoMessage" : "",
                        "electionTime" : Timestamp(1572657665, 1),
                        "electionDate" : ISODate("2019-11-02T01:21:05Z"),
                        "configVersion" : 1,
                        "self" : true,
                        "lastHeartbeatMessage" : ""
                },
                {
                        "_id" : 1,
                        "name" : "node2:27017",
                        "ip" : "172.31.46.39",
                        "health" : 1,
                        "state" : 2,
                        "stateStr" : "SECONDARY",
                        "uptime" : 2397,
                        "optime" : {
                                "ts" : Timestamp(1572657858, 5),
                                "t" : NumberLong(2)
                        },
                        "optimeDurable" : {
                                "ts" : Timestamp(1572657858, 5),
                                "t" : NumberLong(2)
                        },
                        "optimeDate" : ISODate("2019-11-02T01:24:18Z"),
                        "optimeDurableDate" : ISODate("2019-11-02T01:24:18Z"),
                        "lastHeartbeat" : ISODate("2019-11-02T01:24:33.606Z"),
                        "lastHeartbeatRecv" : ISODate("2019-11-02T01:24:33.269Z"),
                        "pingMs" : NumberLong(0),
                        "lastHeartbeatMessage" : "",
                        "syncingTo" : "node1:27017",
                        "syncSourceHost" : "node1:27017",
                        "syncSourceId" : 0,
                        "infoMessage" : "",
                        "configVersion" : 1
                },
                {
                        "_id" : 2,
                        "name" : "node3:27017",
                        "ip" : "172.31.45.70",
                        "health" : 0,
                        "state" : 8,
                        "stateStr" : "(not reachable/healthy)",
                        "uptime" : 0,
                        "optime" : {
                                "ts" : Timestamp(0, 0),
                                "t" : NumberLong(-1)
                        },
                        "optimeDurable" : {
                                "ts" : Timestamp(0, 0),
                                "t" : NumberLong(-1)
                        },
                        "optimeDate" : ISODate("1970-01-01T00:00:00Z"),
                        "optimeDurableDate" : ISODate("1970-01-01T00:00:00Z"),
                        "lastHeartbeat" : ISODate("2019-11-02T01:24:33.171Z"),
                        "lastHeartbeatRecv" : ISODate("2019-11-02T01:21:04.511Z"),
                        "pingMs" : NumberLong(2),
                        "lastHeartbeatMessage" : "Error connecting to node3:27017 (172.31.45.70:27017) :: caused by :: No route to host",
                        "syncingTo" : "",
                        "syncSourceHost" : "",
                        "syncSourceId" : -1,
                        "infoMessage" : "",
                        "configVersion" : -1
                }
        ],
        "ok" : 1,
        "$clusterTime" : {
                "clusterTime" : Timestamp(1572657858, 5),
                "signature" : {
                        "hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
                        "keyId" : NumberLong(0)
                }
        },
        "operationTime" : Timestamp(1572657858, 5)
}




rs.config()
{
        "_id" : "rs0",
        "version" : 1,
        "protocolVersion" : NumberLong(1),
        "writeConcernMajorityJournalDefault" : true,
        "members" : [
                {
                        "_id" : 0,
                        "host" : "node1:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 1,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                },
                {
                        "_id" : 1,
                        "host" : "node2:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 1,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                },
                {
                        "_id" : 2,
                        "host" : "node3:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 1,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                }
        ],
        "settings" : {
                "chainingAllowed" : true,
                "heartbeatIntervalMillis" : 2000,
                "heartbeatTimeoutSecs" : 10,
                "electionTimeoutMillis" : 10000,
                "catchUpTimeoutMillis" : -1,
                "catchUpTakeoverDelayMillis" : 30000,
                "getLastErrorModes" : {

                },
                "getLastErrorDefaults" : {
                        "w" : 1,
                        "wtimeout" : 0
                },
                "replicaSetId" : ObjectId("5dbcd17418f8bd2e75844753")
        }
}
```
