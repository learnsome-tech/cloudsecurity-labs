package platform.buckets_test

import data.platform.buckets

test_owner_can_read if {
    buckets.allow with input as {
        "user": {"name": "ben", "team": "payments"},
        "action": "read",
        "bucket": {"name": "payments-exports", "owner": "payments"},
    }
}

test_delete_without_mfa_is_denied if {
    count(buckets.deny) == 1 with input as {
        "user": {"name": "amara", "team": "platform"},
        "action": "delete",
        "bucket": {"name": "logs-archive", "owner": "security"},
    }
}
