from rest_framework import permissions


class CanViewAllProducts(permissions.BasePermission):
    """
    Custom permission to only allow users with the 'can_view_all_products'
    permission to view all products.
    """

    def has_permission(self, request, view):
        return (request.user and
                request.user.roles.filter(
                    permissions__name='can_view_all_products').exists()
                )


class CanManageOrders(permissions.BasePermission):
    """
    Custom permission to only allow users with the 'can_manage_orders'
    permission to manage orders.
    """

    def has_permission(self, request, view):
        return (request.user and request.user.roles.filter(
            permissions__name='can_manage_orders').exists()
        )


class CanViewAllTransactions(permissions.BasePermission):
    """
    Custom permission to only allow users with the 'can_view_all_transactions'
    permission to view all transactions.
    """
    def has_permission(self, request, view):
        return (request.user and
                request.user.roles.filter(
                    permissions__name='can_view_all_transactions').exists()
                )


class CanManageTransactions(permissions.BasePermission):
    """
    Custom permission to only allow users with the 'can_manage_transactions'
    permission to manage transactions.
    """
    def has_permission(self, request, view):
        return (request.user and
                request.user.roles.filter(
                    permissions__name='can_manage_transactions').exists()
                )


class CanViewAllInvoices(permissions.BasePermission):
    """
    Custom permission to only allow users with the 'can_view_all_invoices'
    permission to view all invoices.
    """
    def has_permission(self, request, view):
        return (request.user and
                request.user.roles.filter(
                    permissions__name='can_view_all_invoices').exists()
                )


class CanManageInvoices(permissions.BasePermission):
    """
    Custom permission to only allow users with the 'can_manage_invoices'
    permission to manage invoices.
    """
    def has_permission(self, request, view):
        return (request.user and
                request.user.roles.filter(
                    permissions__name='can_manage_invoices').exists()
                )
