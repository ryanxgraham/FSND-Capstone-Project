#!/bin/sh
export AUTH0_DOMAIN='rgraham.auth0.com'
export ALGORITHMS=['RS256']
export API_AUDIENCE='capstone'
export CLIENT_ID='TMWB0ZYKbwdiX7DR9ogU4VPzdkXaxGG2'
export assistant_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImUxUHRUNHd0U1BYb1NySERoQzAtUiJ9.eyJpc3MiOiJodHRwczovL3JncmFoYW0uYXV0aDAuY29tLyIsInN1YiI6IlBMMmhrVmQ3S2g1VHQ4NjYwTmdMWWtTWmlGak53anllQGNsaWVudHMiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTU4ODk2NDU2OSwiZXhwIjoxNTkxNTU2NTY5LCJhenAiOiJQTDJoa1ZkN0toNVR0ODY2ME5nTFlrU1ppRmpOd2p5ZSIsInNjb3BlIjoiZ2V0OmFjdG9ycyBnZXQ6bW92aWVzIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.Loms4VuxuQSoUCBkxZsKxyImUnxMQeoZm4-uuOy3wDE1jSVrgQjvl9VQ56k0cfRx4bnw5nA6LDIrLRt5stT-F_EjMGEZ_3WxL-VeMtAowlkOJ841cHwkK02zn7uBNTp6AmkUOzXnXTApKyVNgXZ5RnoOdoYgpEZ1lmqqKDLkmkjo7hCnrTkDg7PyEVDw7kdgPN-ExAjxDd5ioUqe1fvE0V55--X-KYW6lDjeTCiO69M0MygypbgwV-uCwomKHbjR5YvQeMmRD-UAW30jFp7pWCC1UDbLAQw6JQciuePnFhMXUpOBjzARZmER0xFgdVyNMrRqPLegKc80myjAQpRYxw

export director_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImUxUHRUNHd0U1BYb1NySERoQzAtUiJ9.eyJpc3MiOiJodHRwczovL3JncmFoYW0uYXV0aDAuY29tLyIsInN1YiI6IlBMMmhrVmQ3S2g1VHQ4NjYwTmdMWWtTWmlGak53anllQGNsaWVudHMiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTU4ODk2NDUwNiwiZXhwIjoxNTkxNTU2NTA2LCJhenAiOiJQTDJoa1ZkN0toNVR0ODY2ME5nTFlrU1ppRmpOd2p5ZSIsInNjb3BlIjoiZ2V0OmFjdG9ycyBnZXQ6bW92aWVzIGRlbGV0ZTphY3RvcnMgcG9zdDphY3RvcnMgcGF0Y2g6bW92aWVzIHBhdGNoOmFjdG9ycyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwiZGVsZXRlOmFjdG9ycyIsInBvc3Q6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicGF0Y2g6YWN0b3JzIl19.T8L7HpL2wUvrmMLv7T_TSPkWfl2KbOcdiO-14vtvIQoAOikHaVc1KywqbuphTsKQXZ4eYXXQufanCo3nwKkZZEQ4YG8zTwY2BuURDEm5v-YgvAkoiXMAnVb7O_Dj4CxDdgCiUNe0YehqkbONHrlu3GkKdzrXInispk5-WhwG_iIaam518cDhho7sqd8qzOUenNbgRk4xDVkx1RPGbqbgHTUzkPAt2tbUTVBrWiBr3fd0RcM5au3BL3dh8MgKX5u-eDVd0BrCR__KikoNbqD4qe6zAsp5VQLCRdy4Oq7KnpVvvtcDE-bUfbDQnbA-OxfzruvEcvKZPPoqrTkVoGabFQ

export producer_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImUxUHRUNHd0U1BYb1NySERoQzAtUiJ9.eyJpc3MiOiJodHRwczovL3JncmFoYW0uYXV0aDAuY29tLyIsInN1YiI6IlBMMmhrVmQ3S2g1VHQ4NjYwTmdMWWtTWmlGak53anllQGNsaWVudHMiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTU4ODk2NDUwNiwiZXhwIjoxNTkxNTU2NTA2LCJhenAiOiJQTDJoa1ZkN0toNVR0ODY2ME5nTFlrU1ppRmpOd2p5ZSIsInNjb3BlIjoiZ2V0OmFjdG9ycyBnZXQ6bW92aWVzIGRlbGV0ZTphY3RvcnMgcG9zdDphY3RvcnMgcGF0Y2g6bW92aWVzIHBhdGNoOmFjdG9ycyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwiZGVsZXRlOmFjdG9ycyIsInBvc3Q6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicGF0Y2g6YWN0b3JzIl19.T8L7HpL2wUvrmMLv7T_TSPkWfl2KbOcdiO-14vtvIQoAOikHaVc1KywqbuphTsKQXZ4eYXXQufanCo3nwKkZZEQ4YG8zTwY2BuURDEm5v-YgvAkoiXMAnVb7O_Dj4CxDdgCiUNe0YehqkbONHrlu3GkKdzrXInispk5-WhwG_iIaam518cDhho7sqd8qzOUenNbgRk4xDVkx1RPGbqbgHTUzkPAt2tbUTVBrWiBr3fd0RcM5au3BL3dh8MgKX5u-eDVd0BrCR__KikoNbqD4qe6zAsp5VQLCRdy4Oq7KnpVvvtcDE-bUfbDQnbA-OxfzruvEcvKZPPoqrTkVoGabFQ
