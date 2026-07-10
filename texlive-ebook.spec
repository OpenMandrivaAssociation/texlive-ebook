%global tl_name ebook
%global tl_revision 29466

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Helps creating an ebook by providing an ebook class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ebook
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ebook.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ebook.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines a command \ebook that defines page layout, fonts,
and font-sizes for documents to be rendered as PDF-ebooks on small
ebook-readers. The package has been tested with Kindle e-ink and iPad
mini.

