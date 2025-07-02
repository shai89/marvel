def paginate(queryset, page: int, limit: int):
    total = queryset.count()
    items = queryset.offset((page - 1) * limit).limit(limit).all()
    return {
        "total": total,
        "page": page,
        "limit": limit,
        "items": items,
    }
