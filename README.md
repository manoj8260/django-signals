# Django Signals Demo

A Django project demonstrating real-world usage of **Django signals**
including pre-save, post-save, pre-delete, and many-to-many change tracking.

---

## Implemented Signals

- `pre_save` → Automatic slug generation
- `post_save` → User welcome notification
- `pre_delete` → Backup before deletion
- `m2m_changed` → Track tag add/remove actions

---

## Signal Examples

### Automatic Slug Generation
- Triggered before saving a Post
- Generates slug using `slugify(title)`

### User Welcome Notification
- Triggered on User creation
- Sends a welcome message (dummy email)

### Pre-Deletion Backup
- Copies Post data into `DeletedPost`
- Runs before actual deletion

### Many-to-Many Tracking
- Tracks tag additions and removals
- Logs affected tag IDs with timestamps

---

## Run Demo

```bash
python manage.py signals_demo
### Example Output
(env) PS C:\Users\mn047\OneDrive\Desktop\Django-signals\signals> python manage.py signals_demo
>>
Slug: django-signals
Welcome email sent to mn047653@gmail.com
[2026-01-18 14:47:18.048704+00:00] PRE_ADD {5, 6} on Django Signals
[2026-01-18 14:47:18.085408+00:00] POST_REMOVE {5} on Django Signals
DeletedPost count: 1

 SQL QUERIES
INSERT INTO "notifications_post" ("title", "slug") VALUES ('Django Signals', 'django-signals') RETURNING "notifications_post"."id"
INSERT INTO "auth_user" ("password", "last_login", "is_superuser", "username", "first_name", "last_name", "email", "is_staff", "is_active", "date_joined") VALUES ('', NULL, 0, 'manoj', '', '', 'mn047653@gmail.com', 0, 1, '2026-01-18 14:47:17.986355') RETURNING "auth_user"."id"
INSERT INTO "notifications_tag" ("name") VALUES ('Django') RETURNING "notifications_tag"."id"
INSERT INTO "notifications_tag" ("name") VALUES ('Signals') RETURNING "notifications_tag"."id"
BEGIN
SELECT "notifications_post_tags"."tag_id" AS "tag" FROM "notifications_post_tags" WHERE ("notifications_post_tags"."post_id" = 3 AND "notifications_post_tags"."tag_id" IN (5, 6))
INSERT OR IGNORE INTO "notifications_post_tags" ("post_id", "tag_id") VALUES (3, 5), (3, 6)
COMMIT
BEGIN
DELETE FROM "notifications_post_tags" WHERE ("notifications_post_tags"."post_id" = 3 AND "notifications_post_tags"."tag_id" IN (5))
COMMIT
BEGIN
INSERT INTO "notifications_deletedpost" ("title", "slug", "deleted_at") VALUES ('Django Signals', 'django-signals', '2026-01-18 14:47:18.099626') RETURNING "notifications_deletedpost"."id"
DELETE FROM "notifications_post_tags" WHERE "notifications_post_tags"."post_id" IN (3)
DELETE FROM "notifications_post" WHERE "notifications_post"."id" IN (3)
COMMIT
SELECT COUNT(*) AS "__count" FROM "notifications_deletedpost"
