from rest_framework import permissions


class CanViewAllProducts(permissions.BasePermission):
    """
    Custom permission to only allow users with the 'can_view_all_products'
    permission to view all products.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.roles.filter(permissions__name='can_view_all_products').exists()
        return False


class CanManageOrders(permissions.BasePermission):
    """
    Custom permission to only allow users with the 'can_manage_orders'
    permission to manage orders.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.roles.filter(permissions__name='can_manage_orders').exists()
        return False


class CanViewAllTransactions(permissions.BasePermission):
    """
    Custom permission to only allow users with the 'can_view_all_transactions'
    permission to view all transactions.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.roles.filter(permissions__name='can_view_all_transactions').exists()
        return False


class CanManageTransactions(permissions.BasePermission):
    """
    Custom permission to only allow users with the 'can_manage_transactions'
    permission to manage transactions.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.roles.filter(permissions__name='can_manage_transactions').exists()
        return False


class CanViewAllInvoices(permissions.BasePermission):
    """
    Custom permission to only allow users with the 'can_view_all_invoices'
    permission to view all invoices.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.roles.filter(permissions__name='can_view_all_invoices').exists()
        return False


class CanManageInvoices(permissions.BasePermission):
    """
    Custom permission to only allow users with the 'can_manage_invoices'
    permission to manage invoices.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.roles.filter(permissions__name='can_manage_invoices').exists()
        return False
